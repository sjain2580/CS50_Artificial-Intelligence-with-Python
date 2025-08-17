# Parser Project Documentation

Welcome to the documentation for the **Parser** project, part of CS50 AI 2024. The main objective of this project is to implement a program that takes an English sentence as input and produces its most likely **syntactic parse tree**. This tree represents the sentence's hierarchical grammatical structure according to a given set of grammatical rules. The challenge lies in handling **ambiguity** – where a sentence can have multiple valid parse trees – by using probabilities associated with the grammatical rules.
This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project delves into Natural Language Processing (NLP), specifically syntactic parsing, and is a practical application of probabilistic reasoning and dynamic programming in AI.

1. **Input and Output**
- Input: A natural language sentence (e.g., "She saw the man with the telescope.").

- Output: The most probable parse tree for that sentence. A parse tree is a hierarchical structure where:

    - Leaf nodes are the individual words (terminals).

    - Internal nodes are grammatical categories (non-terminals) like Sentence (S), Noun Phrase (NP), Verb Phrase (VP), Prepositional Phrase (PP), Noun (N), Verb (V), Determiner (D), etc.

2. **Core Concepts**
- **Context-Free Grammars (CFGs)**: At its heart, the project uses a CFG, which is a set of production rules that describe how symbols can be rewritten. For example:

S -> NP VP (A Sentence can be a Noun Phrase followed by a Verb Phrase)

NP -> D N (A Noun Phrase can be a Determiner followed by a Noun)

D -> "the" (A Determiner can be the word "the")
The grammar defines all possible valid structures for sentences.

- **Probabilistic Context-Free Grammars (PCFGs)**: Natural language is inherently ambiguous. A sentence like "I saw the man with the telescope" could mean "I saw the man (who had the telescope)" or "I saw (the man using a telescope)." To resolve this, PCFGs assign a probability to each production rule. Rules that are more common in a given language corpus will have higher probabilities. The goal of the parser is to find the parse tree with the highest cumulative probability.

- **Treebank**: The project typically provides access to a treebank, which is a corpus of sentences that have been manually annotated with their correct parse trees. This treebank is crucial for:

    - Learning PCFG Probabilities: By counting how often each production rule occurs in the treebank, the parser can calculate the probabilities for its PCFG.

    - Evaluating Performance: Comparing the parser's output trees to the gold-standard trees in the treebank allows for quantitative evaluation of its accuracy.

- **Parsing Algorithms**: While the specific algorithm might vary, parsing typically involves dynamic programming. A common algorithm for PCFGs is the **CKY (Cocke-Kasami-Young) algorithm** or variants thereof. These algorithms build up parse trees bottom-up (from words to phrases) by considering all possible ways to combine smaller constituents, storing intermediate results to avoid redundant computations, and using probabilities to favor the most likely interpretations.

3. Key Challenges
Ambiguity Resolution: The primary challenge is accurately determining the single most probable parse tree when multiple valid structures exist.

Computational Efficiency: Parsing can be computationally intensive, especially for longer sentences and large grammars. Dynamic programming is essential for managing this complexity.

Grammar Coverage: A good parser relies on a comprehensive grammar. The quality of the learned probabilities from the treebank directly impacts performance.

- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/parser

## Installation

To set up and run the Parser project locally, follow these steps:

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
Contributions to improve the Parser project are welcome! To contribute:

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
