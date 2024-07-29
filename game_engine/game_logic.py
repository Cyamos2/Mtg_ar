# game_logic.py

class GameLogic:
    def __init__(self, players):
        self.players = players
        self.turn = 0

    def start_game(self):
        print("Starting the game...")
        # Initialize game state
        for player in self.players:
            player.draw_initial_hand()

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)
        current_player = self.players[self.turn]
        print(f"It is now {current_player.name}'s turn.")
        # Execute turn logic for current player
        current_player.take_turn()

    def check_winner(self):
        # Check if there is a winner
        for player in self.players:
            if player.has_won():
                print(f"{player.name} has won the game!")
                return player
        return None
