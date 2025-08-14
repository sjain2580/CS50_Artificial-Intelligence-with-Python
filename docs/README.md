# Nim Project Documentation

Welcome to the documentation for the **Nim** project, part of CS50 AI 2024. The main objective of this project is to build a Python program that trains an AI to play the mathematical game of Nim. The AI learns the optimal strategy by playing many games against itself or a random opponent, rather than being explicitly programmed with the rules of optimal play. This demonstrates how an AI can learn to make decisions through trial and error and reinforcement.

This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project is an excellent hands-on introduction to reinforcement learning and how an AI can discover optimal policies for a game.

1. The Game of Nim
**Rules**: Nim is a simple mathematical game of strategy. It's played with several heaps of objects (e.g., coins, stones).

Players take turns.

On a player's turn, they choose one heap and remove one or more objects from that heap.

The player who takes the last object(s) wins (or, in some variants, loses, but CS50 typically uses the "last player wins" rule).

**State Representation**: The state of the game is defined by the number of objects remaining in each heap. For example, (1, 2, 3) represents three heaps with 1, 2, and 3 objects respectively.

2. Reinforcement Learning Approach
The AI for the Nim project doesn't use adversarial search (like Minimax for Tic-Tac-Toe). Instead, it learns by playing many games and associating "rewards" with game outcomes.

**Q-learning (Conceptual)**: While the project might simplify it, the underlying concept is similar to Q-learning or temporal difference learning. The AI builds a "memory" of states and the values of actions from those states.

States and Actions:

**State**: The configuration of the heaps.

**Action**: A pair (heap_index, num_to_remove) indicating which heap to take from and how many objects to remove.

**Knowledge Representation (Q-values/Counts)**: The AI maintains:

    - q (Q-values): A dictionary or table that maps (state, action) pairs to a numerical value representing the estimated "quality" or "expected future reward" of taking that action in that state. Initially, all Q-values are unknown or set to zero.

    - N (Counts): A table that keeps track of how many times the AI has visited a particular (state, action) pair. This helps in exploration (trying new actions).

**Rewards**:

    - Win: If the AI makes a move that leads to a win, it receives a positive reward (e.g., 1).

    - Loss: If the AI makes a move that leads to a loss, it receives a negative reward (e.g., -1).

    - Draw: In Nim, draws are not usually possible if played optimally.

3. **Learning Process (Training)**
The AI learns by playing numerous N games (e.g., 10,000 games) and updating its q and N values.

**Exploration vs. Exploitation**: This is a key dilemma in reinforcement learning.

**Exploration**: The AI sometimes chooses random actions to discover new states and potential optimal paths. This is especially important early in training.

**Exploitation**: The AI sometimes chooses the action with the highest estimated Q-value for the current state, using what it has already learned.

A common strategy is ϵ-greedy exploration, where the AI chooses a random action with probability ϵ and the best-known action with probability 1−ϵ. As training progresses, ϵ often decreases to favor exploitation.

Updating Q-values: After each game, the AI "backpropagates" the final reward through the sequence of moves made in that game.

If a game results in a win, all actions that led to that win are reinforced (their Q-values increase).

If a game results in a loss, actions leading to that loss are penalized (their Q-values decrease).

The update rule typically involves a learning rate (alpha) and a discount factor (gamma), though these might be simplified or implicitly handled in the CS50 version.

4. **Playing a Game (After Training)**
Once trained, the AI can play Nim by always choosing the action with the highest Q-value for the current game state. If multiple actions have the same maximal Q-value, it might choose randomly among them.

5. **Optimal Strategy (Nim-Sum)**
While the AI learns the optimal strategy, the theoretical optimal strategy for Nim involves the Nim-sum (bitwise XOR sum) of the heap sizes. A position is a "P-position" (previous player winning, meaning current player losing) if the Nim-sum is 0, and an "N-position" (next player winning, meaning current player winning) if the Nim-sum is non-zero. An optimal player always moves to a P-position. The AI learns this implicitly.

- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/nim-project
## Installation

To set up and run the Nim project locally, follow these steps:

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
Contributions to improve the Nim project are welcome! To contribute:

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
