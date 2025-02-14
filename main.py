import pytesseract

# Add this line
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Now, load the image and extract text
from PIL import Image
image_path = "delivery_challan_sample.jpeg"
img = Image.open(image_path)
text = pytesseract.image_to_string(img)
print(text)
