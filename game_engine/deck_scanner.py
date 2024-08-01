# game_engine/deck_scanner.py

from .card_recognition import CardRecognition
from .card_validator import CardValidator
from langdetect import detect

class DeckScanner:
    def __init__(self, tesseract_cmd):
        self.card_recognition = CardRecognition(tesseract_cmd)
        self.card_validator = CardValidator("json/card_database.json")

    def scan_deck(self, image_paths):
        scanned_deck = []
        for image_path in image_paths:
            card_text = self.card_recognition.recognize_card(image_path)
            if card_text and self.card_validator.validate_card(card_text):
                scanned_deck.append(card_text)
        return scanned_deck
