## CS50 Traffic: Road Sign Classifier
This project implements a convolutional neural network (CNN) to classify traffic signs from the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The AI learns to recognize 43 different types of road signs, demonstrating fundamental concepts in machine learning, image processing with cv2, and deep learning with tensorflow.

## Experimentation Process and Observations
My approach to building this traffic sign classifier was highly iterative, driven by exploration of cv2 and tensorflow documentation, and observing the model's performance. The core challenge was to design a robust pipeline for data loading and a neural network architecture that could effectively learn complex visual features from images.

## Data Loading and Preprocessing
Initially, my primary focus was on correctly loading the diverse set of images from the 43 subdirectories using cv2.imread. A key aspect was ensuring all images were resized to a uniform IMG_WIDTH x IMG_HEIGHT (30x30 pixels). This consistent input size is critical for neural networks. I decided to retain the 3 color channels (RGB/BGR) rather than converting to grayscale, as color information is often vital for distinguishing traffic signs (e.g., red stop signs vs. blue informational signs). Although I didn't explicitly normalize pixel values (dividing by 255) in the load_data function, tensorflow layers often handle internal scaling. For the labels, tf.keras.utils.to_categorical was essential to convert integer labels into a one-hot encoded format, which is required for multi-class classification with a softmax output layer and categorical_crossentropy loss.

One challenge encountered during data loading was ensuring only actual image files were read, as some datasets might contain hidden files or non-image data. Implementing a check for valid file extensions (.png, .jpg, .ppm etc.) proved crucial to prevent cv2.imread from returning None and causing errors.


## What Worked Well & What Didn't
Worked Well:

The basic CNN architecture (Conv2D -> MaxPooling -> Flatten -> Dense -> Dropout) proved effective for image classification.

Using cv2.imread and cv2.resize was efficient for image handling.

tf.keras.utils.to_categorical was straightforward for label encoding.

The adam optimizer and categorical_crossentropy loss functioned as expected.

The Dropout layer was critical in combating overfitting and improving generalization to unseen data.

Didn't Work Well:

Initial models without Dropout layers heavily overfit the training data.

Incorrectly setting input_shape for the first Conv2D layer (e.g., trying to use 1 channel for grayscale when the images were loaded in 3 channels by default) led to runtime errors.

Hardcoding paths inside the load_data function initially caused issues with command-line argument flexibility. This was resolved by passing data_dir as an argument.

## Key Observations
My experimentation reaffirmed several key principles in deep learning:

Preprocessing is Paramount: Consistent image sizing and proper label encoding are non-negotiable foundations for effective model training.

Iterative Model Design: Building a good model is rarely a one-shot process. It involves iterative adjustments to layers, filters, and other hyperparameters, driven by performance metrics on validation data.

Regularization is Key: For smaller datasets or more complex models, regularization techniques like dropout are essential to prevent the model from simply memorizing the training data.

Documentation is Your Best Friend: Understanding the parameters for functions like cv2.resize, tf.keras.layers.Conv2D, and the various compilation options in tensorflow is crucial. The official documentation provided invaluable guidance throughout the project.

This project was a hands-on exploration of how AI can "see" and classify images, highlighting the interplay between data preparation, neural network design, and careful evaluation.