# Tictactoe Project Documentation

Welcome to the documentation for the **Tictactoe** project, part of CS50 AI 2024. The main objective of this project is to build a Python program that allows a human player to play Tic-Tac-Toe against an AI, or for two AI players to compete against each other. The core challenge lies in developing the AI's "intelligence" to make optimal moves.
This documentation provides an overview, setup instructions, usage details, and insights into the code.



## Overview

The project focuses on applying adversarial search algorithms to a well-known game.

1. Game Representation
The game board is typically represented as a 3x3 grid, often using a 2D list or similar data structure.

The state of the board includes the positions of 'X's, 'O's, and empty squares.

2. Game Rules and Logic
The program must correctly implement the rules of Tic-Tac-Toe:

Players take turns placing their mark ('X' or 'O').

Marks cannot be placed on occupied squares.

The game ends when a player gets three of their marks in a row (horizontally, vertically, or diagonally), or when all squares are filled (a draw).

3. Artificial Intelligence (AI) Implementation
This is the heart of the project. The AI needs to be able to choose the best possible move at any given state of the game. The standard approach for this project is to use the Minimax algorithm:

Minimax Algorithm: This is a decision-making algorithm used in game theory for two-player zero-sum games (where one player's gain is another's loss). It works by:

Exploring the Game Tree: The AI considers all possible future moves from the current state, and all possible counter-moves by the opponent, and so on, building a "game tree" of possible game states.

Evaluating States: For each terminal state (win, lose, or draw), the algorithm assigns a numerical "utility value" (e.g., +1 for a win, -1 for a loss, 0 for a draw).

Minimizing/Maximizing:

The AI player (the "maximizer") chooses the move that leads to the state with the highest utility value for itself.

It assumes the opponent (the "minimizer") will always choose the move that leads to the state with the lowest utility value for the AI.

Optimal Play: By recursively exploring the tree and backing up utility values, Minimax guarantees that the AI will always make the optimal move, assuming the opponent also plays optimally.

4. Optional Enhancements
Alpha-Beta Pruning: An optimization technique for Minimax that drastically reduces the number of nodes that need to be evaluated in the game tree without affecting the final decision. This is often a significant part of the project.

Randomization: If multiple moves have the same optimal utility, the AI might choose one randomly to make its play less predictable (though still optimal).

5. User Interface (Basic)
A simple text-based interface is usually sufficient to display the board and take human player input.

- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/tictactoe-project
## Installation

To set up and run the Heredity project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python.git
   cd sjain2580/CS50_Artificial-Intelligence-with-Python.git

2. **Install Dependencies**:
   Ensure Python 3.12 (or later) is installed:
   ```bash
   python --version

3. **Set up Documentation (Optional)**: 
   Install Docsify to view this documentation locally:
   ```bash
   npm install -g docsify-cli
   cd docs
   docsify serve
   Make necessary changes
   Open http://localhost:3000 to preview.


## Contributing
Contributions to improve the Heredity project are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b branch/your-branch

3. **Make changes and commit**:
   ```bash
   git commit -m "Add your message"

4. **Push to the branch**:
   ```bash
   git push origin branch/your-branch

5. **Open a pull request**:
   Please ensure code follows PEP 8 style guidelines and includes updated documentation.
