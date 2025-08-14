# Knights Project Documentation

Welcome to the documentation for the **Knights** project, part of CS50 AI 2024. The main objective of this project is to write a Python program that can determine the truthfulness of statements made by characters in a "Knights and Knaves" puzzle. In these puzzles, there are two types of inhabitants:

Knights: Always tell the truth.

Knaves: Always lie.

The goal of the AI is to figure out who is a Knight and who is a Knave based on a set of logical statements they make.

This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project delves deep into knowledge representation and logical inference, specifically using a technique called model checking.

1. Knowledge Representation
The first crucial step is to translate the puzzle's rules and the characters' statements into a formal logical language, specifically propositional logic.

Symbols: Each character's identity is represented by a propositional symbol. For example, AKnight could mean "A is a Knight" and AKnave could mean "A is a Knave."

Basic Rules (Axioms): The program must include fundamental logical statements that define the nature of Knights and Knaves:

A character is either a Knight OR a Knave, but NOT both. (e.g., (AKnight OR AKnave) AND NOT (AKnight AND AKnave))

Characters' Statements: Each statement made by a character is translated into a logical implication:

If a character is a Knight, then their statement is true.

If a character is a Knave, then their statement is false (i.e., the negation of their statement is true).

Example: If A says "I am a Knight":

AKnight <=> "I am a Knight" (where "I am a Knight" is translated into propositional logic).

So, AKnight <=> AKnight which is a tautology, simplified to just AKnight.

Example: If A says "I am a Knave":

AKnight <=> "I am a Knave"

So, AKnight <=> AKnave

2. Logical Inference: Model Checking
Once all rules and statements are encoded as propositional logic sentences, the AI uses model checking to find a consistent assignment of truth values (Knight or Knave) to each character.

Models: A "model" is an assignment of truth values (True or False) to all propositional symbols (e.g., AKnight = True, BKnight = False).

Satisfiability: The model checker iterates through all possible combinations of truth assignments for the characters. For each combination (model), it checks if all of the logical sentences (axioms + translated statements) are true in that model.

Consistent Model: Any model where all sentences evaluate to true is a consistent model.

If there's only one consistent model, then the AI has uniquely determined who is a Knight and who is a Knave.

If there are multiple consistent models, the puzzle cannot be uniquely solved (i.e., there are ambiguities).

If there are no consistent models, the puzzle has no solution (i.e., the statements are contradictory).

3. Implementation Details
The project typically provides a basic framework or a logic library (often logic.py) that includes classes for Symbol, And, Or, Not, Implication, Biconditional (for "if and only if"), and a model_check function. Students then:

Define knowledge as a And object combining all axioms and converted statements.

Use model_check to iterate through possible assignments.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/knights-project

## Installation

To set up and run the Knights project locally, follow these steps:

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
Contributions to improve the Knights project are welcome! To contribute:

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
