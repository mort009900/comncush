import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """Extracts text from an image using OCR."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng')
        return text
    except Exception as e:
        print(f"Error extracting text from image {image_path}: {e}")
        return ""