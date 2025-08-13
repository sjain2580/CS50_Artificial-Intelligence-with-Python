# Minesweeper Project Documentation

Welcome to the documentation for the **Minesweeper** project, part of CS50 AI 2024. The main objective of this project is to implement an AI that can play Minesweeper by inferring the location of mines based on numerical clues revealed on the board. The AI needs to use logical deduction and probability to make safe moves and identify potential mine locations, rather than just guessing randomly.
This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project is a fantastic application of knowledge representation and logical inference in artificial intelligence.

1. Game Setup and Mechanics 🎲
Board Representation: The game typically uses a grid (e.g., 8x8, 10x10) with some squares hiding mines.

Squares: Each square can be:

Unrevealed: Hidden from the player.

Revealed (Empty): A safe square with no adjacent mines.

Revealed (Numbered): A safe square showing a number (1-8), indicating how many of its adjacent squares contain mines.

Mine: A square that contains a mine (if revealed, the game ends).

Player Actions:

mark_mine(cell): The player (or AI) marks a square as a suspected mine.

mark_safe(cell): The player (or AI) marks a square as safe.

make_safe_move(): The AI chooses a guaranteed safe square to click.

make_random_move(): If no safe moves can be logically determined, the AI might resort to a random (but un-marked) move.

2. Artificial Intelligence (AI) Core 🧠
The AI's intelligence is built around maintaining and updating a knowledge base about the game board.

Knowledge Base: The AI maintains a set of logical "sentences" or "clauses" that represent its current understanding of the board. Each sentence relates a set of unknown cells to a count of how many mines are among them.

Example: If a revealed square (r, c) shows the number '2', and it has three unrevealed neighbors {(r1, c1), (r2, c2), (r3, c3)}, the AI forms a sentence like: "There are exactly 2 mines in the set {(r1, c1), (r2, c2), (r3, c3)}."

Inference Engine: The AI's ability to deduce new information relies on powerful inference rules:

Subset Rule: This is the most crucial inference. If the AI has two sentences, and one set of unknown cells is a subset of another, then it can derive a new, simpler sentence.

Example:

Sentence 1: "There is 1 mine in {(A, B, C)}" (where A, B, C are cells).

Sentence 2: "There are 2 mines in {(A, B, C, D, E)}"

Since {(A, B, C)} is a subset of {(A, B, C, D, E)}, the AI can deduce that "There is 1 mine in {(D, E)}" (because 2 - 1 = 1 mine in the remaining cells D, E).

Direct Deductions:

If a sentence states "There are 0 mines in S", then all cells in set S are guaranteed safe.

If a sentence states "There are ∣S∣ mines in S" (where ∣S∣ is the number of cells in the set), then all cells in set S are guaranteed to be mines.

3. Game Flow for the AI 🔁
Initial Move: The AI typically makes a random safe move to start (often the first click in Minesweeper is safe by default, or the project might define a way for the AI to pick an initial safe spot).

Process Revealed Information: Whenever a square is clicked and reveals a number:

The AI adds new sentences to its knowledge base based on that number and its unrevealed neighbors.

It also updates existing sentences by removing known safe cells or marked mine cells.

Perform Inference: The AI repeatedly applies its inference rules (especially the subset rule) to its knowledge base to derive new, simpler sentences.

Identify Safe Moves and Mines: Based on the inferred sentences:

Any cell determined to be definitively safe is added to a set of safe_moves.

Any cell determined to be definitively a mine is added to a set of mines.

Make a Move:

If safe_moves is not empty, the AI chooses one of these guaranteed safe moves.

If safe_moves is empty, but there are still unrevealed cells, the AI might resort to a "random safe move" by picking an unrevealed cell that hasn't been logically identified as a mine. This is where the AI takes a calculated risk, but it's often the only option when pure logic can't resolve the board completely.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/minesweeper-project

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
