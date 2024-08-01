# game_engine/card_validator.py

import json

class CardValidator:
    def __init__(self, card_database_path):
        with open(card_database_path, 'r', encoding='utf-8') as f:
            self.card_database = json.load(f)

    def validate_card(self, card_name):
        return card_name in self.card_database
