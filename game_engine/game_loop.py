# game_loop.py

from game_logic import GameLogic

class GameLoop:
    def __init__(self, players):
        self.game_logic = GameLogic(players)

    def run(self):
        self.game_logic.start_game()
        while True:
            winner = self.game_logic.check_winner()
            if winner:
                break
            self.game_logic.next_turn()
