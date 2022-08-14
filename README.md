# recommendation_system
Personalised recommendations of Products to Users

## About
A Recommendation engine recommends products or items present in a group of data to the users according to their likes and preferences.From e-commerce to online advertisement, Recommender systems are used in a variety of areas. It helps to improve the personalized content, better product search experience.

Recommender systems are mainly of 2 types – Content-based Filtering and Collaborative Filtering (Memory-based and Model-based). Using both Implicit and Explicit ratings, companies can recommend relevant content to their users. This project aims to describe a movie recommender system that utilizes explicit ratings and movie genres to make personalized recommendations.

## Goal
Build and compare a movie recommendation system based on ‘MovieLens’ dataset using Content based and Collaborative filtering approach.

## Dataset
The MovieLens Latest Dataset is used which consists of 4 dataset files written in comma-separated values. Prior official permission to use the dataset for this project was obtained from GroupLens. This data set consists of 100,000 ratings (0.5-5) from 9000 movies on 600 users and each user has rated at least 20 movies. The dataset can be found on the GroupLens Official Website.

## Implementation
1. Content-based Filtering - Using TF_IDF and Cosine Similarity Metric
2. Collaborative Filtering - Using deep neural network with user and item embeddings

## Tools and Technology
1. Python 3.9
    - Libraries & Packages: NumPy, Pandas, Matplotlib, Sklearn, Keras, Tensorflow
2. Jupyter Notebook

## Conclusion
Recommender systems provide personalization and help businesses increase profits, and also allow users to find the most relevant products for them to use. The goal of this project is to gain a comprehensive understanding of the various filtration processes and their subsequent technologies. A literature review examines different techniques and their advantages and disadvantages, further guiding the selection of better models and evaluation metrics based on the data. Implementing content-based filtering solves the cold-start problem that is a limitation of collaborative filtering. However, model-based collaborative filtering achieves faster and more efficient results compared to memory-based methods and content-based filtering.

## Future Work
This project covers understanding and implementing basic techniques for building simple recommender systems. Recent studies have shown that the use of hybrid models, deep learning techniques such as RNNs, and extensive hyperparameter tuning of existing models can improve the scalability, performance, and efficiency of these systems. The new hybrid technology can also solve existing problems through individual approaches. Furthermore, the evaluation of the top N recommendations shows a low hit rate, which indicates a lack of implicit ratings and metadata about movies and users. Therefore, more detailed data can help provide more personalized recommendations.

## Installation
These instructions will get you a copy of the project up and running on your local machine
### Clone
Clone this repo to your local machine using ....
### Setup
```
conda env create -f environment.yml
```
 
