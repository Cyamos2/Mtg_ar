# game_engine/game_loop.py

from ai_opponents.jiwon_ai import JiwonAI

def game_loop():
    jiwon = JiwonAI()
    jiwon.setup_game()

    # Placeholder for the player's turn setup
    player_turn = True

    while True:
        if player_turn:
            print("Player's turn")
            # Implement player's turn logic
            player_turn = False
        else:
            print("Jiwon's turn")
            jiwon.play_turn()
            player_turn = True

        # Add logic to check for end of game condition
        if check_game_end(jiwon):
            break

def check_game_end(opponent):
    # Placeholder logic to check for game end conditions
    return False  # Keep game running

if __name__ == "__main__":
    game_loop()
