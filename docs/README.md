# Shopping Project Documentation

Welcome to the documentation for the **Shopping** project, part of CS50 AI 2024. The main objective of this project is to train a machine learning model using a dataset of online user behavior. This dataset typically includes various features derived from a user's session on a shopping website, such as page visit durations, bounce rates, number of product-related pages visited, operating system, browser, etc. The trained model should then be able to take new, unseen user session data and predict the likelihood of that user completing a transaction.

This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project is an excellent introduction to classification algorithms in machine learning, particularly using the **scikit-learn** library. It involves data preprocessing, model training, and evaluation.

1. Dataset
The project typically uses a provided dataset (often a .csv file), where each row represents a user session and columns represent different features. A crucial column is the "Revenue" or "Purchase" column, which is the target variable (whether the user made a purchase, usually a binary 0/1 or True/False).

Examples of features in the dataset might include:

- Page Types: Number of administrative pages, informational pages, product-related pages visited.

- Time Spent: Duration spent on different types of pages.

- Bounce Rate: Percentage of visitors who enter the site and leave immediately.

- Exit Rate: Percentage of visitors who leave the site from a specific page.

- Operating System, Browser, Region, Traffic Type: Categorical features about the user's setup and how they arrived at the site.

- Weekend: Whether the session occurred on a weekend.

- Month: The month of the session.

2. Data Preprocessing
Before training a machine learning model, the raw data needs to be cleaned and transformed:

Categorical to Numerical: Many machine learning algorithms require numerical input. Categorical features (like "Operating System" or "Month") need to be converted into numerical representations. This is often done using:

One-Hot Encoding: Creating new binary columns for each category (e.g., a column OS_Windows, OS_MacOS, where 1 indicates presence and 0 absence).

Feature and Target Separation: The dataset needs to be split into:

Features (X): The input variables used to make predictions.

Target (y): The variable being predicted (e.g., "Revenue").

3. Model Training
The project usually guides students to use a K-Nearest Neighbors (KNN) classifier for this task.

K-Nearest Neighbors (KNN): This is a non-parametric, lazy learning algorithm used for both classification and regression. For classification:

When given a new data point, it finds the 'K' closest data points (neighbors) in the training set.

The new data point is classified based on the majority class among its K nearest neighbors.

Splitting Data: The dataset is typically split into:

Training Set: Used to train the model.

Testing Set: Used to evaluate the model's performance on unseen data. This prevents overfitting. The train_test_split function from sklearn.model_selection is commonly used for this.

4. Model Evaluation
After training, the model's performance is assessed using metrics relevant to classification:

Accuracy: The proportion of correctly classified instances (both purchases and non-purchases).

Sensitivity (Recall): The proportion of actual positive cases (users who did purchase) that were correctly identified by the model. This is crucial for not missing potential customers.

Specificity: The proportion of actual negative cases (users who did not purchase) that were correctly identified.

The project emphasizes that while accuracy is important, sensitivity is often a more critical metric in this context, as a business would rather incorrectly predict a non-buyer as a buyer (false positive) than miss a real buyer (false negative).

- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/shopping-project
## Installation

To set up and run the Shopping project locally, follow these steps:

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
