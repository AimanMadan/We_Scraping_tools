import os
import pytesseract
from PIL import Image

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'"C:/Program Files/Tesseract-OCR/tesseract.exe"'  # Change this path as necessary

# Path to the Article directory
article_dir = 'C:/Users/aiman/Documents/thankful2plants/Articles'

# Function to process each image
def process_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Failed to process image {image_path}: {e}")
        return None

# Walk through all the directories and files in the Article directory
for root, dirs, files in os.walk(article_dir):
    for file in files:
        file_path = os.path.join(root, file)
        # Check if the file is an image (you can add more image extensions if needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            text = process_image(file_path)
            if text:
                # Create a text file with the same name as the image file
                text_file_path = os.path.splitext(file_path)[0] + '.txt'
                with open(text_file_path, 'w') as text_file:
                    text_file.write(text)
                # Delete the image file
                os.remove(file_path)
                print(f"Processed and deleted image: {file_path}")

print("Processing complete.")
