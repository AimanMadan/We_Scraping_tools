# Web Scraping and OCR Project

This repository contains three Python scripts for web scraping and image processing. These scripts fetch URLs, extract text and images, and process images to extract text using OCR.

## Project Structure

- `getData.py`: Fetches content from given URLs, extracts main text and images, and stores them in separate directories.
- `getLinks.py`: Scrapes URLs from 'onclick' attributes of `li` elements in the given URLs.
- `imageToText.py`: Processes images in a specified directory to extract text using Tesseract OCR.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `pytesseract`
  - `Pillow`

You can install the required packages using the following command:

```sh
pip install requests beautifulsoup4 pytesseract pillow
```

Additionally, you need to install Tesseract OCR. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

## Usage

### 1. `getLinks.py`

This script scrapes URLs from 'onclick' attributes of `li` elements in the provided URLs and saves them to a file.

```sh
python getLinks.py
```

1. Create a file named `input_urls.txt` and add the URLs you want to scrape, one per line.
2. Run the script.

The scraped URLs will be saved in `scraped_urls.txt`.

### 2. `getData.py`

This script fetches content from URLs, extracts main text and images, and stores them in separate directories.

```sh
python getData.py
```

1. Ensure `scraped_urls.txt` (created from the previous step) is in the same directory.
2. Run the script.

The content will be saved in directories named `article_1`, `article_2`, etc.

### 3. `imageToText.py`

This script processes images in a specified directory to extract text using Tesseract OCR.

```sh
python imageToText.py
```

1. Update the `article_dir` variable to point to the directory containing your images.
2. Run the script.

The extracted text will be saved in text files with the same names as the images, and the original images will be deleted.

## Configuration

- Update the Tesseract executable path in `imageToText.py` to match your Tesseract installation.

```python
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
```

- Update the `article_dir` variable in `imageToText.py` to point to the directory containing your images.

```python
article_dir = 'C:/Users/aiman/Documents/thankful2plants/Articles'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/en/latest/)

