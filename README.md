# URL Text and Image Extractor

## Description

This Python script is a tool designed to extract text and images from URLs provided by the user. It extracts the main text content from `<p>` and `<span>` tags and downloads all images, ignoring those with filenames containing 'logo' or 'gmail_icon'. For each URL provided, it creates a new folder (article_1, article_2, etc.) to store the extracted text and images.

## Features

- Extracts text from `<p>` and `<span>` tags.
- Downloads images, excluding those with 'logo' or 'gmail_icon' in their filenames.
- Creates a new directory for each URL to store the text and images.

## Installation

To use this script, you need to have Python installed on your machine. You also need to install the required libraries:

```bash
pip install beautifulsoup4 requests
