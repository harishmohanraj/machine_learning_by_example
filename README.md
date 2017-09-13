# Machine Learning by Example:
# What is Machine Learning:
    - Machine learning is a sub field of artificial intelligence.
    - By definition it is the "computer's the ability to learn without being explicitly programmed"
    - Machine learning explores the study and construction of algorithms that can learn from and make
      predictions on data without being explicitly programmed.
    - Machine Learning is all about learning form examples and experience rather than writing manual rules
    - One program that can solve many problems without being rewritten.
    - You write a lot of manual rules to solve the problem, in machine learning you let the algorithm decide
      for you from examples.

### Training data and Testing data:
    - In machine learning train your algorithm in a different dataset and test it with a different dataset.
    - Save 10% of your data as test_dataset and train the algorithm with the remaining 90% of the data and
      finally test the accuracy of the algorithm with the 10% of data.

### Classifier:
    - A classifier (eg. decision tree) is a function, it takes data(features) as input and assigns label
      to it as output
    - The technique to automatically write the classifier is called **Supervised learning**

# Supervise Learning
    - Creating a classifier by finding patterns in examples
    - First we will collect the training data(examples of the problem we want to solve)

## Supervised Classifications:
    - You have a bunch of examples and your know which is the rite one

#### In machine leaning we will input features and try to get labels out of it.
Example:
- Identifying the songs based on Features
    - in this use case are
        - Intensity of the song
        - Tempo of the song
        - Genre
        - Gender of the voice
- Based of the above input(Features) the brain decides between 2 things
    - Like
    - Don’t Like

## Decision surface:
    - Its the line separates one class from another class whether it can generalize to never before
    seen data point.

## Bayse Rule:

    - In probability theory and statistics, Bayes’ theorem (alternatively Bayes’ law or Bayes' rule) describes the probability of an event, based on prior
    knowledge of conditions that might be related to the event.
    - For example, if cancer is related to age, then, using Bayes’ theorem, a person’s age can be used to more
    accurately assess the probability that they have cancer, compared to the assessment of the probability of cancer made without knowledge of the person's age.

## Naive Bayes Strengths:
    - Easy to implement.
    - Requires small amount of training data to estimate the parameters.
    - Good results obtained in most of the cases.
    - Naive Bayes is particularly useful for Natural Language Processing ( text classification).
    - [link to comparision ](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/)

## Naive Bayes Weaknesses:


## SVM(Support Vector Machines)
- Puts first and foremost the correct of the labels and then maximizes the margin

# Decision Tree
    - Decision Trees (DTs) are a non-parametric supervised
      learning method used for classification and regression.
    - The goal is to create a model that predicts the value
      of a target variable by learning simple decision rules
      inferred from the data features.
### Entropy:
    - controls how a decision tree decides where to split the data
    - by definition "measure of impurity in a bunch of examples"
    - Formula for entropy is
    - minimum value for entropy is 0 and the maximum value it can take is 1.0
### Information gain:
    - is the (entropy of the parent) - (the weighted average of the entropy of the children)
    - the decision tree algorithm will maximize the information gain
### Strength:
    - Easy to use
    - Can be graphically interpeted
### Weakness:
    - Prone to overfitting, specially if you have a data that's have lots and lots of features and a complicated decision tree
      it can overfit the data's

# Ensemble Machine learning algorithm:
    - Ensembles are a divide and conquire approach used to
      improve performance to improve generalizability
      / robustness over a single estimator.
    - The main principle behind Ensemble methods is
      that a group of weak learner can come together
      to form a strong learner.
    - Each classifier is individually a weak learner
      while the classifier taken together are a strong
      learner and thus ensemble methods reduce inference
      and improve performance.

### Two families of ensemble methods are usually distinguished:
#### Average Methods:
    - In averaging methods, the driving principle is to build
      several estimators independently and then to average their predictions.
      On average, the combined estimator is usually
      better than any of the single base estimator because its
      variance is reduced.
        - Examples: Bagging methods, Forests of randomized trees
#### Boosting Methods:
    - By contrast, in boosting methods, base estimators are
      built sequentially and one tries to reduce the bias of
      the combined estimator. The motivation is to combine
      several weak models to produce a powerful ensemble.
        - Examples: AdaBoost, Gradient Tree Boosting, …
# Random Forests (Average Methods):
    - Is  one of the most popular and most powerful supervised classification
      algorithm that is capable of performing both regression and
      classification task.
    - This algorithm creates a forest with a number of decision trees.
    - The more tree in the forest the more robest is the prediction and
      thus higher accuracy
    - Random forest algorithm is also known as "Ensemble Machine
      learning algorithm"
### How Random Forest algorithm works:
    - In random forest we grow multiple tree as supposed to a single tree.
    - To classify a new object based on attributes, each tree gives a
      classification. The forest choses the classification having the
      most votes over all the other trees in the forest.
    - In the case of regression the forest takes the average
      of the output of different trees.
### Strengths:
    - Same algorithm can be used for both classification and regression tasks.
    - Won't overfit the model like decision trees
    - Handles large dataset with higher dimensionality
### Weakness:
    - Good for classification problems but not so good for regression.
    - In case of regression you have very little control on what the model does.
### Application of Ramdon Forest algorithm:
    - We can use random forest algorithm in banking sector.
        - e.g.Finding loyal customers and freaud customers
    - Can be used in medicine where we identify the correct combination of
      components to validate medicine
    - Also help's in analysing the patients diesease based on the medical records
    - In stock market random forest algorithm is used to identify the stock
      peak behavior as well as the expected loss/profit before purchasing a
      particular stock.
    - In e-comerce random forest algorithm is used in small segment of the
      recommendation engine for identifying the likelyhood of a customer
      liking the recomended products.
    - In computer vision the random forset algorithm is for image classification,           Microsoft used random forset algorithm in X-box in small segment.

