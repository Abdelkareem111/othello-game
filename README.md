# Othello Game (Reversi) — Pygame Edition

A classic implementation of the Othello board game using **Pygame**, featuring:

- Player vs. Player mode  
- Player vs. AI mode with difficulty levels  
- Interactive GUI with menus and animations

---

## Getting Started

Clone this repository and run the game:

```bash
git clone https://github.com/Abdelkareem111/othello-game.git
cd othello-game
python main.py
```

Make sure you have [Pygame](https://www.pygame.org/news) installed:

```bash
pip install pygame
```

---

## How to Play

The game follows the standard **Othello rules**:

- Players take turns placing pieces on the board.
- You must place your piece so that it **brackets** one or more of the opponent's pieces in any direction (horizontal, vertical, or diagonal).
- Bracketed opponent pieces are **flipped to your color**.
- The game ends when **no valid moves** remain for either player.
- **Black always goes first**.

---

## Controls

- 🖱️ **Mouse Click**: Place your piece  
- 🖱️ **Mouse Hover**: Highlight buttons in menus  
- 🖱️ **Click on Winner Screen**: Return to main menu

---

## Code Structure

- `OthelloGame`: Core game logic (board state, valid move checks, AI decisions).
- `Button`: Handles clickable UI buttons and menu interactions.
- `draw_*` functions: Render game board, menus, scores, and end screens.
- `main.py`: Entry point that connects all components.

---

## Contributing

Contributions and suggestions are welcome!  
Feel free to **fork the repo** and submit a **pull request** with improvements, features, or bug fixes.

---

## License

This project is licensed under the **MIT License** — free to use and modify.
```
