# card_recognition.py

import pytesseract
from PIL import Image

class CardRecognition:
    def __init__(self, tesseract_cmd):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def recognize_card(self, image_path):
        # Load image
        image = Image.open(image_path)
        # Use Tesseract to do OCR on the image
        card_text = pytesseract.image_to_string(image)
        return card_text.strip()

    def recognize_deck(self, image_paths):
        recognized_cards = []
        for image_path in image_paths:
            recognized_cards.append(self.recognize_card(image_path))
        return recognized_cards
