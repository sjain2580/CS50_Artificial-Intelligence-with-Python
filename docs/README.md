# Attention Project Documentation

Welcome to the documentation for the **Attention** project, part of CS50 AI 2024. The main objective of this project typically involves implementing or utilizing components of a Transformer-based model (like BERT) to perform a masked language modeling task. In this task, the AI is given a sentence where one or more words are "masked" (hidden), and its job is to predict the original masked words based on the context provided by the unmasked words. A key part of the project is visualizing the self-attention weights, which helps in understanding how the model focuses on different words in the input sentence to make its predictions. 
This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project provides a practical understanding of key concepts in modern Natural Language Processing (NLP) and deep learning architectures.

1. **Self-Attention**
At the heart of the project is the concept of self-attention.

- What it is: Self-attention is a mechanism that allows a model to weigh the importance of different words in an input sequence (e.g., a sentence) when processing a particular word in that same sequence. Instead of processing words sequentially or relying on fixed-size windows, self-attention can capture long-range dependencies and relationships between words, regardless of their distance in the sentence.

- How it works (conceptually): For each word in a sentence, the model calculates an "attention score" with every other word in the sentence. These scores determine how much "focus" or "attention" the model places on each surrounding word when trying to understand or represent the current word. Words that are highly relevant to the meaning or context of the current word will receive higher attention scores.

2. **Transformer Models (e.g., BERT)**
The project utilizes or builds upon Transformer models, which are deep neural networks that heavily rely on the self-attention mechanism.

- Architecture: Transformers eschew traditional recurrent (RNNs) or convolutional (CNNs) layers for sequences, instead using stacked layers of multi-head self-attention and feed-forward networks.

- BERT (Bidirectional Encoder Representations from Transformers): A prominent pre-trained Transformer model, often used in this project. BERT is designed to understand context in text bidirectionally (looking at words before and after a given word).

3. **Masked Language Model (MLM) Task**
This is the specific task often used to demonstrate and train the attention mechanism.

- The Goal: Given a sentence with some words replaced by a [MASK] token, the model must predict the original masked words.

- How it relates to attention: To accurately predict a masked word, the model needs to understand the context. Self-attention allows it to look at all other words in the sentence and determine which ones are most relevant to inferring the masked word. For example, in "The [MASK] barked loudly," the model would likely attend heavily to "barked" to predict "dog."

4. **Visualization of Attention Scores**
A critical component of this project is to visualize the attention weights.

- Purpose: By generating heatmaps or diagrams, you can see exactly which words a particular "attention head" (a sub-component within a Transformer's attention mechanism) is focusing on when processing each word.

- Interpretation: These visualizations provide insights into how the model makes decisions, revealing linguistic relationships (e.g., subject-verb agreement, pronoun-antecedent links, relationships between nouns and adjectives) that the model has implicitly learned. For instance, when the model processes a pronoun like "he," an attention head might show strong attention to the noun it refers to earlier in the sentence.

5. **Key Libraries**
- transformers: Hugging Face's transformers library is commonly used for this project. It provides easy access to pre-trained Transformer models like BERT and their tokenizers, as well as tools to extract attention weights.

- tensorflow: Used as the backend framework for building and running the neural network models.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/attention

## Installation

To set up and run the Attention project locally, follow these steps:

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
Contributions to improve the Attention project are welcome! To contribute:

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
