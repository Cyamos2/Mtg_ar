# game_engine/load_deck.py

import json

class DeckLoader:
    def load_deck(self, deck_path):
        with open(deck_path, 'r') as f:
            return json.load(f)
