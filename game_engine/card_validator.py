# card_validator.py

class CardValidator:
    def __init__(self, card_database):
        self.card_database = card_database

    def validate_cards(self, scanned_deck):
        valid_cards = [card for card in scanned_deck if card in self.card_database]
        invalid_cards = [card for card in scanned_deck if card not in self.card_database]
        return valid_cards, invalid_cards
