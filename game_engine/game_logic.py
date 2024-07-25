class Game:
    def __init__(self, ai_opponent):
        self.ai_opponent = ai_opponent
        self.player_life_total = 40

    def is_over(self):
        return self.player_life_total <= 0 or self.ai_opponent.life_total <= 0

    def player_turn(self):
        # Implement player turn logic
        print("Player's turn")

    def ai_turn(self):
        print("AI's turn")
        self.ai_opponent.take_turn()
