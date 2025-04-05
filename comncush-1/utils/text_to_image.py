def extract_text_from_image(image_path):
    import pytesseract
    from PIL import Image

    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img, lang='eng')
    
    return text