# Othello Game

A Python implementation of the classic Othello (Reversi) board game with both single-player and two-player modes.

## Features

- Play against AI with three difficulty levels:
  - Easy: Makes random moves occasionally
  - Medium: Balanced AI with occasional mistakes
  - Hard: Strategic AI that always chooses the best move
- Play against a friend in two-player mode
- Real-time score tracking
- Valid move indicators
- Clear winner announcement
- Modern user interface

## Requirements

- Python 3.x
- Pygame

## Installation

1. Make sure you have Python installed on your system
2. Install Pygame using pip:
```bash
pip install pygame
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Choose your game mode:
   - vs Computer: Play against the AI
   - vs Friend: Play with another person

3. If you choose vs Computer, select difficulty:
   - Easy: Good for beginners
   - Medium: Balanced challenge
   - Hard: Strategic and challenging

4. Game Rules:
   - Black moves first
   - Click on valid positions (marked with gray dots)
   - Pieces are flipped when trapped between two opponent pieces
   - Game ends when no valid moves remain
   - Player with the most pieces wins

## Controls

- Mouse click: Make a move
- Click anywhere after game over to return to menu
- Close window to quit game

## File Structure

- `main.py`: Main game loop and control flow
- `game.py`: Game logic and AI implementation
- `display.py`: All display and rendering functions
- `button.py`: Button class for menu interface
- `constants.py`: Game constants and configuration