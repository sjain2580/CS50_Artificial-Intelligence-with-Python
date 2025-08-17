# Crossword Project Documentation

Welcome to the documentation for the **Crossword** project, part of CS50 AI 2024. The main objective of this project is to write a Python program that takes a crossword puzzle structure and a list of words, then uses AI techniques to fill the grid optimally to create a valid and solvable crossword puzzle. The AI must ensure that all words fit the given structure and that intersecting letters match.
This documentation provides an overview, setup instructions, usage details, and insights into the code.

## Overview

This project is a classic application of **Constraint Satisfaction Problems (CSPs)** and **backtracking search** in artificial intelligence.

1. **Input and Output**
- **Input**:
    - Puzzle Structure: A text file or similar representation defining the crossword grid. This includes:

    - The dimensions of the grid (rows, columns).

    - Which cells are empty (where words can go) and which are blocked (black squares).

    - The "variables" of the crossword: the starting position, direction (across/down), and length of each word slot.

- **Word** List: A text file containing a dictionary of valid words that can be used to fill the puzzle.

- **Output**:

    - A filled crossword puzzle grid, typically saved as an image, with words placed correctly according to the structure and the constraints.

2. **Core Concepts: Constraint Satisfaction Problem (CSP)**
The problem is framed as a CSP, which consists of:

- **Variables**: Each "slot" or "square" in the crossword grid where a word can be placed (defined by its start, direction, and length). The domain of each variable is the set of all possible words from the given word list that fit the length of that slot.

- **Domains**: For each variable, the domain is the set of all words from the provided list that have the correct length to fit that specific slot.

- **Constraints**: These are the rules that must be satisfied for a valid puzzle:

    - All-Different Constraint: Every word placed in the puzzle must be unique (no word used twice).

    - Arc Consistency / Intersecting Letters: If two word slots intersect, the letters at their intersection point must be identical. This is the most crucial constraint.

3. **AI Algorithm: Backtracking Search**
The primary algorithm used to solve the CSP is **backtracking search**:

**Initialization**: Start with an empty grid (no words assigned to slots).

**Variable Selection**: Choose an unassigned variable (an empty word slot). Good heuristics for variable selection can significantly improve performance:

**Minimum Remaining Values (MRV)**: Choose the variable with the fewest remaining valid words in its domain (i.e., the most constrained variable).

**Degree Heuristic**: If there's a tie in MRV, choose the variable that has the most constraints on other unassigned variables (i.e., the one that intersects with the most other slots).

**Value Ordering**: Once a variable is chosen, try assigning a value (a word) from its domain. Heuristics for value ordering can help:

- Least Constraining Value: Try words that rule out the fewest values from the domains of neighboring variables.

**Constraint Propagation**: After assigning a value:

- Inference: Propagate the effects of the assignment. This means reducing the domains of any other variables that share intersecting cells. If a word is placed, its intersecting letters constrain the possible words for the intersecting slots.

- Failure Detection: If at any point, an assignment leads to an empty domain for another variable (meaning no word can fit there), then the current path of assignments has failed.

**Backtracking**: If a path fails, "backtrack" to the most recent decision point (the last variable assignment) and try a different word for that variable. If all words for that variable have been tried, backtrack further.

**Solution**: The search continues until all variables are assigned values that satisfy all constraints, resulting in a complete and valid crossword puzzle.

4. **Advanced Techniques**
**Arc Consistency (AC-3)**: While basic constraint propagation is part of backtracking, fully implementing AC-3 can prune domains more aggressively before or during search, making the search more efficient.

**Inference inference() function**: This typically removes words from the domains of variables when they conflict with a new assignment.

- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/crossword-project

## Installation

To set up and run the Crossword project locally, follow these steps:

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
Contributions to improve the Crossword project are welcome! To contribute:

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
