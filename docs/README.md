# Pagerank Project Documentation

Welcome to the documentation for the **Pagerank** project, part of CS50 AI 2024. The main objective of this project is to write a Python program that calculates the PageRank of web pages within a given "corpus" (a collection of web pages). The importance of a page is determined by the number and quality of links pointing to it. Pages linked to by many important pages are themselves considered important.
This documentation provides an overview, setup instructions, usage details, and insights into the code.



## Overview

The project requires students to implement two different approaches to calculating PageRank, both based on fundamental concepts of probability and graph theory:

1. Data Representation 📊
The project provides a simplified "corpus" of web pages, typically represented by a directory containing text files. Each file represents a web page and contains links to other pages within the corpus.

The program needs to parse these files to build a data structure (e.g., a dictionary or graph representation) that maps each page to the set of pages it links to.

2. PageRank Algorithm Implementations
The core of the project involves implementing PageRank using two distinct methods:

a. The Random Surfer Model (Sampling Method)
This approach simulates a "random surfer" who navigates the web:

With a certain probability (the damping factor, usually 0.85), the surfer clicks on a random link on the current page.

With the remaining probability (1−damping factor), the surfer "teleports" to any random page in the entire corpus.

The PageRank of a page is estimated by the proportion of time the random surfer spends on that page over a very large number of steps (e.g., 10,000 to 100,000 simulations).

This method is intuitive and probabilistic, providing an approximation of PageRank.

b. The Iterative Algorithm (Markov Chain Method)
This approach directly applies a mathematical formula based on Markov chains to calculate PageRank. It's more precise and converges to the exact PageRank values.

The formula states that a page's PageRank is a function of:

The sum of the PageRanks of all pages that link to it, divided by the number of outbound links from those pages.

A base probability (derived from the damping factor and the total number of pages) that accounts for the random teleportation.

The algorithm starts with an initial arbitrary PageRank distribution (e.g., all pages having equal PageRank) and then iteratively updates these values until they converge (i.e., the changes between iterations fall below a small threshold).

The core formula for PageRank PR(p) of a page p is:

PR(p)= 
N
1−d
​
 +d 
i∈L(p)
∑
​
  
NumLinks(i)
PR(i)
​
 

Where:

d is the damping factor.

N is the total number of pages in the corpus.

L(p) is the set of pages that link to page p.

PR(i) is the PageRank of a page i that links to p.

NumLinks(i) is the number of outbound links from page i.

A special case usually handled: If a page has no outbound links, it's assumed to link to all pages in the corpus (including itself) with equal probability.

3. Evaluation
Students typically need to demonstrate that both methods yield similar PageRank values (within an acceptable tolerance), showcasing the probabilistic and iterative nature of the algorithm.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/degrees-project
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
