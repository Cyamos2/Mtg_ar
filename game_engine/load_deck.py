# load_deck.py

import os

class DeckLoader:
    def __init__(self, decks_folder):
        self.decks_folder = decks_folder

    def load_deck(self, deck_name):
        deck_path = os.path.join(self.decks_folder, f"{deck_name}.txt")
        if not os.path.exists(deck_path):
            raise FileNotFoundError(f"Deck file '{deck_name}.txt' not found in '{self.decks_folder}'.")

        deck = []
        with open(deck_path, 'r', encoding='utf-8') as file:
            for line in file:
                card_name = line.strip()
                if card_name:
                    deck.append(card_name)
        return deck

# Example usage:
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    decks_folder = os.path.join(base_dir, '..', 'decks')
    loader = DeckLoader(decks_folder)

    # Example deck names
    deck_name = "jiwon_rin_and_seri"
    try:
        deck = loader.load_deck(deck_name)
        print(f"Loaded Deck '{deck_name}':")
        print(deck)
    except FileNotFoundError as e:
        print(e)
