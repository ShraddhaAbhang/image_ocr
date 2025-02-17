import cv2
import numpy as np
from PIL import Image

def preprocess_image(image_path, threshold=True):
    """
    Preprocess the image: Convert to grayscale and apply thresholding.
    :param image_path: Path to the image file
    :param threshold: Apply thresholding to remove noise (default: True)
    :return: Preprocessed PIL Image
    """
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if threshold:
        # Apply thresholding to remove noise
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return Image.fromarray(thresh)  # Convert back to PIL format

    return Image.fromarray(gray)
