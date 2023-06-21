# Extract Text from Images

This Python script is used to extract text from a folder of images using Optical Character Recognition (OCR). It can process images in multiple subfolders, apply basic image preprocessing steps, and save the extracted text into separate files for each subfolder. It also supports a debug mode where the preprocessed images are saved for inspection.

## How it works

The script first prompts the user for the folder containing the images (.jpg, .jpeg, .png). It then processes the images using the following steps:

1. Convert the image to grayscale.
2. Sharpen the image.
3. Increase contrast with autocontrast.

These preprocessing steps are applied to enhance the image quality for better OCR results. It then performs OCR on the preprocessed image using Tesseract-OCR `pytesseract` to extract text from the images and saves the results in text files corresponding to each subfolder in the original directory.

If no text was extracted from an image, it will be noted in the text file. Images that had no text extracted are also printed to the console at the end.

## Requirements

This script requires Python 3.6 or higher and the following Python libraries:

- `os`
- `pytesseract`
- `sys`
- `pillow` (Python Imaging Library)
- `unicodedata`
- `concurrent.futures`
- `threading`
- `datetime`
- `time`

You also need to have [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) installed on your system.

## Installation

1. Ensure that Python 3.6 or higher is installed on your system.
2. Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to your system's PATH.
3. Install the required Python packages with pip:

```bash
pip install pillow pytesseract
```

## Usage

1. Save your images in a folder in the same directory as the script. The script will also process images in subfolders.
2. Run the script with the command `python extract_text_from_images.py`
3. Enter the name of the folder containing the images when prompted.
4. The script will process the images and save the extracted text to a series of text files, one for each subfolder. The files will be saved in the original directory and named in the format `subfolder_extracted_text_timestamp.txt`.

### Debug Mode

To save preprocessed images for debugging purposes, add the `--debug` flag when running the script, use the command `python extract_text_from_images.py --debug`.

This will create a "debug_preprocessed_images" folder within the main folder, containing the preprocessed images organized by subfolder.

## Output

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

Images that had no text extracted are also printed to the console at the end.

## Notes

The script currently supports .jpg, .jpeg, and .png image formats.

It is set to use the English language for OCR by default. To use another language, change the `lang` variable in the script to the desired language code (e.g., 'fra' for French).

This script uses Tesseract-OCR, an open-source OCR engine. It assumes that Tesseract-OCR is installed in the default location on a Windows system. If you have installed Tesseract-OCR in a different location, or if you're using a different operating system, you will need to modify the `tesseract_path` variable in the script.

This script performs simple image preprocessing steps to improve the accuracy of the OCR. However, the effectiveness of these steps may vary depending on the quality and characteristics of the input images.

The script uses a thread pool to process multiple images in parallel, which can significantly improve performance when processing a large number of images. However, the maximum number of threads is determined by the system's hardware capabilities.
