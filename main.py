from game_engine.game_logic import Game
from ai_opponents.jiwon_ai import JiwonAI
from decks.jiwon_deck import jiwon_deck

def main():
    # Initialize the game with AI opponent Jiwon
    jiwon_ai = JiwonAI(jiwon_deck)
    game = Game(ai_opponent=jiwon_ai)
    
    # Main game loop
    while not game.is_over():
        game.player_turn()
        game.ai_turn()

if __name__ == "__main__":
    main()
