# deck_scanner.py

from langdetect import detect
import pytesseract
from PIL import Image
import json
import os

class DeckScanner:
    def __init__(self, tesseract_cmd, card_database_path):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.card_database = self.load_card_database(card_database_path)

    def load_card_database(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def scan_deck(self, image_paths):
        scanned_deck = []
        for image_path in image_paths:
            card_name = self.recognize_card(image_path)
            if card_name:
                scanned_deck.append(card_name)
        return scanned_deck

    def recognize_card(self, image_path):
        # Load image
        image = Image.open(image_path)
        # Use Tesseract to do OCR on the image
        card_text = pytesseract.image_to_string(image).strip()
        # Detect the language of the card text
        card_language = detect(card_text)
        # Match card name with the card database
        card_name = self.match_card_name(card_text, card_language)
        return card_name

    def match_card_name(self, card_text, card_language):
        if card_language not in self.card_database:
            return None
        for card in self.card_database[card_language]:
            if card_text.lower() == card.lower():
                return card
        return None

# Example usage:
if __name__ == "__main__":
    tesseract_cmd = "/usr/local/bin/tesseract"  # Adjust this path based on your Tesseract installation
    base_dir = os.path.dirname(os.path.abspath(__file__))
    card_database_path = os.path.join(base_dir, '..', 'data', 'card_database.json')
    scanner = DeckScanner(tesseract_cmd, card_database_path)

    # Example image paths of scanned cards
    image_paths = ["card1.jpg", "card2.jpg", "card3.jpg"]
    scanned_deck = scanner.scan_deck(image_paths)
    print("Scanned Deck:", scanned_deck)
