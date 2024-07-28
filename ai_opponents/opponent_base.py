# ai_opponents/opponent_base.py

class OpponentBase:
    def __init__(self, name, deck, difficulty):
        self.name = name
        self.deck = deck
        self.difficulty = difficulty
        self.hand = []
        self.battlefield = []
        self.graveyard = []
        self.library = self.deck[:]  # Make a copy of the deck for the library

    def shuffle_deck(self):
        import random
        random.shuffle(self.library)

    def draw_card(self):
        if self.library:
            card = self.library.pop(0)
            self.hand.append(card)
            return card
        return None

    def play_turn(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def respond_to_spell(self, spell):
        raise NotImplementedError("This method should be overridden by subclasses")

    def setup_game(self):
        self.shuffle_deck()
        for _ in range(7):  # Draw initial 7 cards
            self.draw_card()

    def show_hand(self):
        return self.hand
