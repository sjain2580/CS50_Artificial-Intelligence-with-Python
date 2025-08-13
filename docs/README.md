# Heredity Project Documentation

Welcome to the documentation for the **Heredity** project, part of CS50 AI 2024. The main objective of this project is to build a Python program that analyzes a family's genetic data to determine the probabilities of individuals:

- Having a specific number of copies of a gene (0, 1, or 2).

- Exhibiting a particular genetic trait.

This involves working with concepts like Mendelian inheritance, probabilities, and how they propagate through a family tree.
This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project is an excellent application of probabilistic graphical models, specifically Bayesian networks, to a real-world biological problem.

1. Data Representation
The project typically provides a dataset detailing family relationships (parents, children) and observed traits (whether an individual exhibits a specific genetic trait).

Each individual in the family tree becomes a node in a conceptual network.

2. Genetic Model (Axioms)
The core of the probabilistic reasoning lies in the rules of Mendelian inheritance:

Gene Inheritance: When a child is born, they inherit one copy of each gene from each parent. The probability of inheriting a specific gene copy from a parent is 0.5.

Gene to Trait Relationship: A specific genetic trait is influenced by the number of copies of a particular gene an individual has. The project defines probabilities for expressing the trait based on having 0, 1, or 2 copies of the gene. These probabilities are given (e.g., P(trait∣0 genes), P(trait∣1 gene), P(trait∣2 genes)).

New Mutation: There's also a small probability (e.g., 0.01) that a gene might mutate and appear in a child even if neither parent passed it on.

3. Probabilistic Inference (Bayesian Network / Enumeration)
The main task is to calculate the probability of each individual having 0, 1, or 2 gene copies, and having the trait, given the observed data and the genetic model. This is done using inference by enumeration over a Bayesian network.

States: For each person, there are possible states for the gene count (0, 1, or 2) and for the trait (true or false).

Joint Probability Distribution: The goal is to compute the joint probability distribution over all possible assignments of gene counts and traits for everyone in the family. This is effectively enumerating all possible "models" of gene counts and traits for all individuals.

Calculating Probabilities: For each possible assignment, the program calculates its probability by multiplying conditional probabilities:

For each person, the probability of their gene count depends on their parents' gene counts (if they have parents in the data).

The probability of their trait depends on their own gene count.

For individuals with no parents in the dataset, their gene counts have a base probability (accounting for mutation).

Conditioning on Evidence: The program takes the "observed" traits as evidence. When calculating probabilities, it only considers those joint assignments that are consistent with the observed traits (i.e., if someone is observed to have a trait, only assignments where they have the trait are considered).

Marginalization: Finally, to find the probability of a specific individual having 0, 1, or 2 genes (or a specific trait), the program sums the probabilities of all joint assignments that are consistent with that specific outcome, conditioned on the evidence.

4. Implementation Details
The project typically involves:

Loading data from CSV files.

Representing the family tree and gene/trait probabilities.

Implementing recursive functions to calculate conditional probabilities for each individual based on their parents.

Iterating through all possible combinations of gene counts for individuals and calculating the probability of each combination, considering the observed traits.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/heredity-project

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
