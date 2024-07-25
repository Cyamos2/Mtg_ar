# Mtg_ar
Augmented Reality for Magic: the Gathering. It is where you can play against AI opponents.

# Magic: The Gathering Augmented Reality AI Opponents

This project is an augmented reality (AR) simulator for Magic: The Gathering with AI opponents and voice command capabilities.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the main program:
    ```bash
    python main.py
    ```

## Directory Structure

- `ai_opponents/`: Contains AI opponent classes.
- `decks/`: Contains deck configurations.
- `game_engine/`: Contains core game logic and voice command handling.
- `main.py`: Entry point of the application.
- `requirements.txt`: List of dependencies.
- `README.md`: Project description and setup instructions.

## Adding New AI Opponents

1. Create a new AI class in `ai_opponents/`.
2. Define the deck in `decks/`.
3. Update `main.py` to include the new AI opponent.

## License

MIT License
