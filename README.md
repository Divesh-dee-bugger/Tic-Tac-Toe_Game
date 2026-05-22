# Tic-Tac-Toe using Griding

A terminal-based Tic-Tac-Toe game created to demonstrate the practical use of the **Griding** Python module in building interactive grid-based applications and games.

This project mainly focuses on showcasing how Griding can manage and control a 2D game board structure in a clean and structured way.

---

# Purpose of This Project

This project was made primarily as a **demonstration project** for the Griding module.

The goal is to show how Griding can be used in real-world applications such as:

- Board games
- Tile systems
- Grid-based simulations
- Terminal applications
- 2D game logic systems

This project is **not intended to be a polished production-ready game**.

---

# Features

- Fully playable terminal Tic-Tac-Toe
- Two-player gameplay
- Automatic win detection
- Automatic draw detection
- Clean grid rendering
- Built completely using the Griding module

---

# Important Notes

- This project is currently **Windows only**
- Some bugs may still exist
- Proper error handling has not been fully implemented yet
- The project was created mainly to demonstrate the capabilities of the Griding module rather than to build a complete commercial-quality game

---

# How To Play

When the game starts, you will first see a **Reference Grid**:

```text
1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
```

Each number represents a position on the board.

Players take turns entering the number corresponding to the cell where they want to place their symbol.

Example:

```text
Enter for X: 5
```

This places `X` in the center cell.

---

# Rules

- Player 1 uses `X`
- Player 2 uses `O`
- Players take turns alternately
- The first player to align 3 symbols:
  - horizontally
  - vertically
  - diagonally
  wins the game
- If all cells are filled and nobody wins, the match ends in a draw

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Divesh-dee-bugger/Tic-Tac-Toe_Game.git
```

---

## Move Into the Project Directory

```bash
cd Tic-Tac-Toe_Game
```

---

# Running the Game

## Option 1 — Directly Run the EXE (Recommended for Playing)

Simply run/open:

```text
game.exe
```

No Python installation is required for this method.

---

## Option 2 — Run Using Python Source Code

### Install Dependencies

This project includes a `requirements.txt` file.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

### Run the Game

```bash
python game.py
```

---

# Technologies Used

- Python
- Griding
- art

---

# About Griding

Griding is a Python module originally developed by Divesh himself for simplifying the creation and management of structured 2D grid-based systems and applications.

The Tic-Tac-Toe game presented in this repository has also been developed by Divesh using his own Griding module in order to demonstrate its practical implementation in interactive grid-based software and game development.

The module is designed for applications such as:

- Grid-based games
- Simulations
- Matrix operations
- Tile systems
- Board engines
- Structured 2D data management

Official Griding Repository:  
https://github.com/Divesh-dee-bugger/Griding

---

# Author

Made with 💖 by Divesh
