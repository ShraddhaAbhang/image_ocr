import pytesseract
from PIL import Image

# Set Tesseract path (Only required if not in system PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path, preprocess_func=None, lang="eng"):
    """
    Extract text from an image using Tesseract OCR.
    
    :param image_path: Path to the image file
    :param preprocess_func: Function to preprocess image (optional)
    :param lang: Language code (default: English)
    :return: Extracted text as a string
    """
    if preprocess_func:
        img = preprocess_func(image_path)  # Apply preprocessing
    else:
        img = Image.open(image_path)  # Load original image
    
    text = pytesseract.image_to_string(img, lang=lang)
    return text.strip()
