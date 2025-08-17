# Traffic Project Documentation

Welcome to the documentation for the **Traffic** project, part of CS50 AI 2024. The main objective of this project to develop a Python program that trains a convolutional neural network (CNN). This CNN learns to recognize and categorize various traffic signs from images within a provided dataset, typically the German Traffic Sign Recognition Benchmark (GTSRB). The AI must process these images and predict which of the 43 possible road sign categories each image belongs to.
This documentation provides an overview, setup instructions, usage details, and insights into the code.


## Overview

This project serves as a practical introduction to image classification using deep learning, specifically focusing on CNNs with the tensorflow and cv2 (OpenCV) libraries.

1. Dataset
The project utilizes a dataset, like GTSRB, which is structured with a root directory containing 43 subdirectories. Each numbered subdirectory represents a unique traffic sign category (e.g., 0 for "Speed limit (20km/h)", 1 for "Speed limit (30km/h)", etc.). Inside each category directory are multiple images of that specific road sign.

2. Data Preprocessing
Before a neural network can learn from images, the raw data requires significant preprocessing:

   - Image Loading: Images are loaded using cv2.imread.

   - Resizing: All images must be resized to a uniform dimension (e.g., 30x30 pixels) to ensure consistent input size for the CNN.

   - Channel Handling: Images are typically kept in their 3-channel color format (RGB/BGR), as color is a vital distinguishing feature for many traffic signs.

   - Label Encoding: The integer labels (0-42) for each category need to be converted into a one-hot encoded format (e.g., category 5 becomes [0,0,0,0,0,1,0,...]). This is crucial for multi-class classification with a softmax output layer and categorical_crossentropy loss.

   - Splitting Data: The loaded data (images and labels) is divided into training and testing sets using sklearn.model_selection.train_test_split. The training set is used to teach the model, while the testing set evaluates its performance on unseen data to prevent overfitting.

3. **Model Training (CNN)**
The core of the project is building and training a Convolutional Neural Network (CNN). CNNs are highly effective for image recognition tasks because they can automatically learn hierarchical features from pixel data.

   - Layers: A typical CNN architecture for this project includes:

   - Conv2D Layers: These are the primary feature extractors, applying filters to the image to detect patterns like edges, textures, and shapes. Rectified Linear Unit (relu) activation is commonly used for non-linearity.

   - MaxPooling2D Layers: These layers reduce the spatial dimensions of the feature maps, which helps in reducing computation and making the learned features more robust to small variations in the image.

   - Flatten Layer: Converts the 2D feature maps into a 1D vector to be fed into fully connected layers.

   - Dense (Hidden) Layers: Standard neural network layers that learn more abstract combinations of features.

   - Dropout Layer: A crucial regularization technique that randomly deactivates a percentage of neurons during training. This prevents the model from relying too heavily on specific features, thereby reducinng overfitting and improving the model's ability to generalize to new images.

   - Output Layer: A final Dense layer with 43 units (one for each category) and a softmax activation function. softmax outputs a probability distribution over the 43 classes, indicating the model's confidence for each sign type.

   - Compilation: The model is compiled with:

   - Optimizer: Often adam, which efficiently adjusts model weights during training.

   - Loss Function: categorical_crossentropy, suitable for multi-class classification with one-hot encoded labels.

   - Metrics: accuracy, to monitor the proportion of correctly classified signs during training and evaluation.

4. **Evaluation**
After training, the model's performance is evaluated on the separate testing set to assess its generalization capabilities. The key metric is accuracy, which indicates how often the model correctly predicts the traffic sign category.


- **Author**: Sakshi Jain
- **Course**: CS50's Introduction to Artificial Intelligence with Python
- **Repository**: https://github.com/sjain2580/CS50_Artificial-Intelligence-with-Python/tree/traffic
## Installation

To set up and run the Traffic project locally, follow these steps:

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
Contributions to improve the Traffic project are welcome! To contribute:

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
