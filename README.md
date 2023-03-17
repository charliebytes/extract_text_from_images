# Image OCR to Text

This script extracts text from images in a specified folder and its subfolders using OCR (Optical Character Recognition). The extracted text is saved to individual text files for each subfolder, and a list of images with no text extracted is displayed at the end.

## How it works

The script first prompts the user for the folder containing the images. It then processes the images using the following steps:

1. Convert the image to grayscale.
2. Sharpen the image.
3. Increase contrast with autocontrast.

These preprocessing steps are applied to enhance the image quality for better OCR results. The script then uses pytesseract to extract text from the preprocessed images and saves the results in text files.

## Requirements

- Python 3.6 or higher
- Pillow (Python Imaging Library)
- pytesseract
- Tesseract OCR

## Installation

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system's PATH.
2. Install the required Python packages:

```bash
pip install Pillow pytesseract
```

## Usage

1. Place the script in the same directory as the folder containing the images.
2. Run the script:

```bash
python image_ocr_to_text.py
```

3. Enter the name of the folder containing the images when prompted.
4. The script will process the images and save the extracted text to individual text files in the main folder.

### Debug Mode

To save preprocessed images for debugging purposes, add the `--debug` flag when running the script:

```bash
python image_ocr_to_text.py --debug
```

This will create a "debug_preprocessed_images" folder within the main folder, containing the preprocessed images organized by subfolder.

## Output format

The script generates a text file for each subfolder with the following format:

```
image_filename.ext
Extracted text from the image

image_filename2.ext
Extracted text from the image

...
```

If no text is extracted from an image, the output will be:

```
image_filename.ext
**NO TEXT EXTRACTED**
```

## Notes

- The script currently supports .jpg, .jpeg, and .png image formats.
- It is set to use the English language for OCR by default. To use another language, change the `lang` variable in the script to the desired language code (e.g., 'fra' for French).
# Image OCR to Text

This script extracts text from images in a specified folder and its subfolders using OCR (Optical Character Recognition). The extracted text is saved to individual text files for each subfolder, and a list of images with no text extracted is displayed at the end.

## How it works

The script first prompts the user for the folder containing the images. It then processes the images using the following steps:

1. Convert the image to grayscale.
2. Sharpen the image.
3. Increase contrast with autocontrast.

These preprocessing steps are applied to enhance the image quality for better OCR results. The script then uses pytesseract to extract text from the preprocessed images and saves the results in text files.

## Requirements

- Python 3.6 or higher
- Pillow (Python Imaging Library)
- pytesseract
- Tesseract OCR

## Installation

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system's PATH.
2. Install the required Python packages:

```bash
pip install Pillow pytesseract
```

## Usage

1. Place the script in the same directory as the folder containing the images.
2. Run the script:

```bash
python image_ocr_to_text.py
```

3. Enter the name of the folder containing the images when prompted.
4. The script will process the images and save the extracted text to individual text files in the main folder.

### Debug Mode

To save preprocessed images for debugging purposes, add the `--debug` flag when running the script:

```bash
python image_ocr_to_text.py --debug
```

This will create a "debug_preprocessed_images" folder within the main folder, containing the preprocessed images organized by subfolder.

## Output format

The script generates a text file for each subfolder with the following format:

```
image_filename.ext
Extracted text from the image

image_filename2.ext
Extracted text from the image

...
```

If no text is extracted from an image, the output will be:

```
image_filename.ext
**NO TEXT EXTRACTED**
```

## Notes

- The script currently supports .jpg, .jpeg, and .png image formats.
- It is set to use the English language for OCR by default. To use another language, change the `lang` variable in the script to the desired language code (e.g., 'fra' for French).
