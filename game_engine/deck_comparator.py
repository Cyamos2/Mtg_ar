# deck_comparator.py

class DeckComparator:
    def __init__(self, predefined_deck):
        self.predefined_deck = predefined_deck

    def compare_decks(self, scanned_deck):
        matched = [card for card in scanned_deck if card in self.predefined_deck]
        missing = [card for card in self.predefined_deck if card not in scanned_deck]
        extras = [card for card in scanned_deck if card not in self.predefined_deck]
        return matched, missing, extras
