import os

def merge_text_files(root_dir, output_file_path):
    combined_text = ""
    
    # Iterate through all subdirectories
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(subdir, file)
                # Extract the article number from the file path
                article_number = os.path.basename(subdir).split('_')[-1]
                try:
                    with open(file_path, 'r') as f:
                        file_content = f.read()
                        combined_text += f"Text from article_{article_number}:\n{file_content}\n\n"
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    # Save combined text to a file
    with open(output_file_path, "w") as file:
        file.write(combined_text)
    
    print(f"Text has been merged and saved to {output_file_path}")

# Root directory containing article subfolders with .txt files
root_dir = r"C:\Users\aiman\Documents\thankful2plants\Articles\Articles"

# Output file path
output_file_path = r"C:\Users\aiman\Documents\thankful2plants\Articles\Articles\merged_text.txt"

# Merge text from all .txt files in articles subfolders and save to file
merge_text_files(root_dir, output_file_path)
