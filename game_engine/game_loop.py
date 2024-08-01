# game_engine/game_loop.py

from .game_logic import GameLogic

class GameLoop:
    def __init__(self):
        self.game_logic = GameLogic()

    def start_game(self, players):
        game_state = self.initialize_game_state(players)
        while not self.game_logic.check_win_conditions(game_state):
            for player in players:
                self.game_logic.process_turn(player, game_state)

    def initialize_game_state(self, players):
        # Initialize game state here
        return {}
