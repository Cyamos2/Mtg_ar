# game_engine/card_recognition.py

import pytesseract
from PIL import Image

class CardRecognition:
    def __init__(self, tesseract_cmd):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def recognize_card(self, image_path):
        image = Image.open(image_path)
        return pytesseract.image_to_string(image).strip()
