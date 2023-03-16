import os
import pytesseract
import sys
from PIL import Image, ImageFilter, ImageOps
import unicodedata
from concurrent.futures import ThreadPoolExecutor
import threading
import datetime
import time

# Prompt the user for the folder containing the images
folder_name = input("Enter the name of the folder containing the images: ")

# Check if the folder exists, otherwise exit with an error
if not os.path.exists(folder_name):
    print(f"Error: The folder '{folder_name}' does not exist.")
    exit()

# Set up OCR engine
home = os.path.expanduser('~')
tesseract_path = os.path.join(home, r'AppData\Local\Programs\Tesseract-OCR\tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path
# Set OCR language
lang = 'eng'

# Check if the '--debug' flag is present in command-line arguments
save_preprocessed_images = '--debug' in sys.argv

# Define a function to process each image
def process_image(filepath):
    filename = os.path.basename(filepath)
    # Skip non-image files
    if not filename.endswith((".jpg", ".jpeg", ".png")):
        return None

    # Open the image and apply preprocessing
    with Image.open(filepath) as image:
        image = image.convert('L')  # Convert to grayscale
        image = image.filter(ImageFilter.SHARPEN)  # Sharpen edges
        image = ImageOps.autocontrast(image, cutoff=1)  # Increase contrast

        # Save preprocessed images if the '--debug' flag is set
        if save_preprocessed_images:
            preprocessed_folder = os.path.join(folder_name, "debug_preprocessed_images", os.path.dirname(os.path.relpath(filepath, folder_name)))
            os.makedirs(preprocessed_folder, exist_ok=True)
            preprocessed_path = os.path.join(preprocessed_folder, filename)
            image.save(preprocessed_path, "PNG")

        # Perform OCR on the preprocessed image
        text = pytesseract.image_to_string(image, lang=lang)
        # Remove line breaks and join text
        text = ' '.join(text.split())
        # Remove non-unicode characters
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

        # Return a tuple with the filepath and text if the text is not empty, otherwise return the filepath and None
        return (filepath, text) if text else (filepath, None)

# Recursively process all images in subfolders
image_files = []
for root, _, files in os.walk(folder_name):
    for file in files:
        if file.endswith((".jpg", ".jpeg", ".png")):
            image_files.append(os.path.join(root, file))

# Function to display a simple text animation
def text_animation():
    sys.stdout.write("\nExtracting text from images")
    while not processing_done:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(3.33)

processing_done = False

# Start the text animation in a separate thread
animation_thread = threading.Thread(target=text_animation)
animation_thread.start()

# Process images in parallel using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    results = list(executor.map(process_image, image_files))

# Signal the animation thread to stop
processing_done = True
animation_thread.join()

# Group results by subfolder
results_by_subfolder = {}
for result in results:
    if result is not None:
        subfolder = os.path.relpath(os.path.dirname(result[0]), folder_name)
        if subfolder not in results_by_subfolder:
            results_by_subfolder[subfolder] = []
        results_by_subfolder[subfolder].append(result)

# Write the extracted text to output files
unprocessed_images = []
for subfolder, subfolder_results in results_by_subfolder.items():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{folder_name}/{subfolder}_extracted_text_{timestamp}.txt"
    
    with open(output_file, "w") as text_file:
        for result in subfolder_results:
            if result[1] is not None:
                # Write the filename and extracted text to the output file
                text_file.write(f"{os.path.basename(result[0])}\n{result[1]}\n\n")
            else:
                # Write the filename and "NO TEXT EXTRACTED" to the output file
                text_file.write(f"{os.path.basename(result[0])}\n**NO TEXT EXTRACTED**\n\n")
                # Append unprocessed images to the list
                unprocessed_images.append(result[0])

# Print unprocessed images
if unprocessed_images:
    print("\n\nImages that had no text extracted:")
    for image in unprocessed_images:
        print(f"{os.path.relpath(image, folder_name)}")

print("\nDone!\n")
