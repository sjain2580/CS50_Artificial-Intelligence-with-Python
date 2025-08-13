# Degrees Project Documentation

Welcome to the documentation for the **Degrees** project, part of CS50 AI 2024. The main objective of this project is to determine the "degrees of separation" between any two given actors. This means finding the shortest chain of movies that connects them, where each link in the chain represents two actors who appeared in the same movie.
This documentation provides an overview, setup instructions, usage details, and insights into the code.



## Overview

The core of the project involves finding the shortest path of on-screen collaborations between two actors. This is achieved by modeling the problem as a graph search problem:

- Nodes: Each actor is represented as a node (or vertex).

- Edges: A connection (edge) exists between two actors if they have appeared in the same movie. The movie itself serves as the "edge" connecting them.

The goal is to find the minimum number of steps (movies and intervening actors) required to link the starting actor to the target actor.

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
