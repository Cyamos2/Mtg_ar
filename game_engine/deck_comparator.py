# game_engine/deck_comparator.py

class DeckComparator:
    def compare_decks(self, deck1, deck2):
        common_cards = set(deck1) & set(deck2)
        unique_to_deck1 = set(deck1) - set(deck2)
        unique_to_deck2 = set(deck2) - set(deck1)
        return common_cards, unique_to_deck1, unique_to_deck2
