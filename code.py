import os
import logging
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Set use_angle_cls to True for better performance on rotated text

def extract_text_from_image(image_path):
    """Extract text using PaddleOCR"""
    try:
        # Use PaddleOCR to read text
        result = ocr.ocr(image_path, cls=True)

        if result:
            # Join the text extracted from the image parts
            text = "\n".join([line[1][0] for line in result[0]])
            return text.strip()
        else:
            return "No text detected"
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {str(e)}")
        return f"Error processing {image_path}: {str(e)}"

def process_images_in_directory(directory_path, output_file):
    """Process images in a directory and save extracted text to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    logging.info(f"Processing: {filename}")
                    text = extract_text_from_image(file_path)
                    f.write(f"{filename}:\n{text}\n\n")
                else:
                    logging.info(f"Skipping non-image file: {filename}")
        logging.info(f"Text extracted and saved to {output_file}")
    except Exception as e:
        logging.error(f"Error in processing directory {directory_path}: {str(e)}")

def main():
    directory_path = "/Users/rajnarayansharma/Desktop/Competetive Prog/assignment/Data/Task1"
    output_file = "/Users/rajnarayansharma/Desktop/Competetive Prog/assignment/outputTask1.txt"
    process_images_in_directory(directory_path, output_file)

if __name__ == "__main__":
    main()
