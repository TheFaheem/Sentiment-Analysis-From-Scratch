<h1 align="center"> Sentiment Analysis From Scratch </h1>

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

This repository contains all the necessary modules from preparing, preprocessing, data generator all the way up to training, evaluating and performing inference for building a sentiment analysis model from scratch using the IMDB Movie Reviews Dataset. This model is designed to classify movie review or a sentence as either positive or negative based on their sentiment.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

Sentiment analysis is the process of determining the sentiment or emotion expressed in a piece of text. This project focuses on building a sentiment analysis model without relying on pre-trained models. My Goal is to understand the step-by-step process of data preparation, preprocessing, model training, and evaluation, which is Fulfilled.

## Repository Structure

- `dataset_initializer.py`: an Utility Class for downloading and preparing the IMDB Movie Reviews Dataset Folder.
- `data_preparer.py`: an Utility Class for processing the dataset folder, preparing the dataset and building vocabulary.
- `dataset_preprocessor.py`: an Utility Class for preprocessing the dataset and preparing tokenization methods for training.
- `batch_iterator.py`: an Utility Class for generating batches of data during model training and testing.
- `activation.py`: A Class for Activation Module used in Model's Architecture.
- `embedding_layers.py` : A Class for Embedding Layer Modules.
- `mha.py`: A Class for Multi Head Attention Module used in our Model's Architecture.
- `transformer_block.py`: A Class for Single Transformer Block used in our Model.
- `encoder.py`: A Class for Encoder Part of Transformer's Architecture, which encapsulate all the modules which we build for Modelling.
- `main.py`: An Example script which encapsulate all the above Modules, Demonstrating initialization, preparation, preprocessing, training the sentiment analysis model, evaluating and performing inference on them.

## Getting Started

To Get Started, follow these steps:

1. **Clone the repository**:
   ```shell
   git clone https://github.com/TheFaheem/Sentiment-Analysis-From-Scratch.git
   cd Sentiment-Analysis-From-Scratch
   ```
2. **Install the Required Libraries**:
   ```shell
   pip install -r requirements.txt
   ```
   
## Usage

If you want to replicate this project and train your own sentiment analysis model or If you want to modify the code used to train the model, you can modify the modules according to your need or preference and train it by, Follow these steps:

- **Setup the Arguments**: Open the `config.yaml`, and set your prefered configuration for training. Now everything is ready to train your own sentiment analysis model.

- **Train**: After Setting up Everything, Fire up the training by running the following in your terminal.
  ```shell
  python main.py
  ```

### Note:

If You are training the model in your local machine, if you have GPUs and it's appropriate drivers are correctly installed in your system, Training will be faster according to what GPU you are using. In case if you don't have GPUs in your local machine then your model will be trained on your cpu, I recommend you to train you're model in cloud because training a model on cpu is embarrassingly slow according to your model's parameter and your cpu type. Don't Worry if you don't want to pay cloud providers to train your model unless your model's parameter count is more than 40 million, I'll Recommend you to check Google Colab (GPU: T4), Kaggle Notebook (GPU: (T4, P100)), Paperspace(GPU: k80) which is sufficient to training your model which has upto 30-40 million trainable parameters, Over 40 million parameters the training will be slower and the runtime can be disconnected anytime without notifying. That's really something to concerned about (Imagine you're runtime is disconnected in last epoch). Anyways it's up to you.

## Contributing

Contributions are valuable and greatly appreciated. By contributing, you help improve this project and make it better for everyone. If you want to this project to adapt any dataset, any model or whatever you're idea is, Below are guidelines to help you get started:

### Ways to Contribute

- **Bug Reports**: If you encounter any issues, bugs, or unexpected behavior while using the project, please [open an issue](https://github.com/TheFaheem/Sentiment-Analysis-From-Scratch/issues) with detailed information about the problem. Be sure to include the steps to reproduce the issue.

- **Feature Requests**: If you have an idea for a new feature or enhancement, feel free to [open an issue](https://github.com/your-username/sentiment-analysis-from-scratch/issues) to discuss it. We value your proposal and will consider your suggestions.

- **Pull Requests**: If you have a solution to an existing issue or an improvement you'd like to contribute, you can submit a pull request. Here's how:
    - Fork the repository to your GitHub account.
    - Create a new branch for your contribution.
    - Make your changes and commit them.
    - Push your changes to your forked repository.
    - Open a pull request against the `main` branch of this repository.
 
### Get in Touch

If you have any questions or need help, feel free to reach out by opening an issue or joining the discussion in existing issues.

### Guidelines

- Comment your code where necessary to make it more understandable to others.
- Make sure your code is well-tested before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/TheFaheem/Sentiment-Analysis-From-Scratch/blob/main/LICENSE) file for details.

  
   
