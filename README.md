# Machine Learning by Example:
# Machine Learning:
    - Machine learning is a sub field of artificial intelligence.
    - By definition it is the "computer's the ability to learn without being explicitly programmed"
    - Machine learning explores the study and construction of algorithms that can learn from and make
      predictions on data without being explicitly programmed.
    - Machine Learning is all about learning form examples and experience rather than writing manual rules
        - E.g. You write a lot of manual rules to solve the problem, in machine learning you let the algorithm decide
      for you from examples.
#### In machine leaning we will input features and try to get labels out of it.
Example:
- Identifying the songs based on Features in this usecase the features can be
        - Intensity of the song
        - Tempo of the song
        - Genre
        - Gender of the voice
- Based of the above input(Features) the machine learning algorithm(classifier) decides between 2 things
    - Like
    - Don’t Like

### Classifier:
    - A classifier (eg. decision tree, SVM) is a function, it takes data(features) as input and assigns label
      to it as output
    - The technique to automatically write the classifier is called **Supervised learning**
### Types of classifications:
    - The computer is presented with example inputs and their desired outputs, and the goal is to learn a general rule that maps inputs to outputs.
    - There are two major types of classification
        - Supervised classification
        - Unsupervised classification
            - No labels are given to the learning algorithm, leaving it on its own to find structure in its input. Unsupervised learning can be a goal in itself (discovering hidden patterns in data) or a means towards an end (feature learning).
# Supervised classification
    - The computer is presented with example inputs and their desired outputs, given by a “teacher”, and the goal is to learn a general rule that maps inputs to outputs.
### Types in supervised classifications:
    - In classification problems we are trying to predict a discrete number of values.
        - The labels(y) generally comes in categorical form and represents a finite number of classes. Consider the tasks bellow:
            - Given set of input features predict whether a Breast Cancer is Benign or Malignant.
            - Given an image correctly classify as containing Cats or Dogs.
            - From a given email predict whether it’s spam email or not.
### Types of classification
    - Binary classification — when there is only two classes to predict, usually 1 or 0 values.
    - Multi-Class Classification — When there are more than two class labels to predict we call multi-classification task. E.g. predicting 3 types of iris species, image classification problems where there are more than thousands classes(cat, dog, fish, car,…).

###Algorithms used for classification
    - Decision Trees
    - Naive Bayes
    - K Nearest Neighbors
    - SVM's
    - etc
### Supervised classification is of two types
    1) Classification
    2) Regression

### Classification VS Regression
    - Classification: Discrete valued Y (e.g. 1,2,3 and 4)
    - Regression: Continues Values Y (e.g. 222.6, 300, 568,…)
    - Whenever you find machine learning problem first define whether you are dealing with a classification or regression problem and you can get to know that analyzing the target variable (Y), note that here the input X can of any kind (continues or discrete) that doesn’t count to define the problem. After defining the problem and getting to know the data it’s much easier to chose or try out some algorithms.

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
    - Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression.
    - The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
### Entropy in Decision Tree:
    - controls how a decision tree decides where to split the data by definition "measure of impurity in a bunch of examples" Formula for entropy is minimum value for entropy is 0 and the maximum value it can take is 1.0
### Information gain in Decision Tree:
    - is the (entropy of the parent) - (the weighted average of the entropy of the children)
    - the decision tree algorithm will maximize the information gain
### Strength:
    - Easy to use
    - Can be graphically interpeted
### Weakness:
    - Prone to overfitting, specially if you have a data that's have lots and lots of features and a complicated decision tree it can overfit the data's
# Ensemble Machine learning algorithm:
    - Ensembles are a divide and conquire approach used to improve performance to improve   generalizability / robustness over a single estimator.
    - The main principle behind Ensemble methods is that a group of weak learner can come   together to form a strong learner.
    - Each classifier is individually a weak learner while the classifier taken together    are a strong learner and thus ensemble methods reduce inference and improve performance.

### Two families of ensemble methods are usually distinguished:
#### Average Methods:
    - In averaging methods, the driving principle is to build
      several estimators independently and then to average their predictions.
      On average, the combined estimator is usually better than any of the single base estimator because its variance is reduced.
        - Examples: Bagging methods, Forests of randomized trees
#### Boosting Methods:
    - By contrast, in boosting methods, base estimators are built sequentially and one tries to reduce the bias of the combined estimator. The motivation is to combine several weak models to produce a powerful ensemble.
        - Examples: AdaBoost, Gradient Tree Boosting, …
# Random Forests (Average Methods):
    - Is  one of the most popular and most powerful supervised classification algorithm that is capable of performing both regression and classification task.
    - This algorithm creates a forest with a number of decision trees.
    - The more tree in the forest the more robest is the prediction and thus higher accuracy
    - Random forest algorithm is also known as "Ensemble Machine learning algorithm"
### How Random Forest algorithm works:
    - In random forest we grow multiple tree as supposed to a single tree.
    - To classify a new object based on attributes, each tree gives a classification. The forest choses the classification having the most votes over all the other trees in the forest.
    - In the case of regression the forest takes the average of the output of different trees.
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
    - Can be used in medicine where we identify the correct combination of components to validate medicine
    - Also help's in analysing the patients diesease based on the medical records
    - In stock market random forest algorithm is used to identify the stock peak behavior as well as the expected loss/profit before purchasing a particular stock.
    - In e-comerce random forest algorithm is used in small segment of the recommendation engine for identifying the likelyhood of a customer liking the recomended products.
    - In computer vision the random forset algorithm is for image classification, Microsoft used random forset algorithm in X-box in small segment.

# Regression:
    - In regression problems we trying to predict continues valued output, take this example. Given a size of the house predict the price(real value).
###Regression Algorithms
    - Linear Regression
    - Regression Trees(e.g. Random Forest)
    - Support Vector Regression (SVR)
    etc
### Slope and Intercept:
    - In the equation y= m(x) + c
        - x is the value of x axis
        - y is the value of y axis
        - m is the value of slope
        - c is the intercept
### Popular Linear regression algorithms:
    - Ordinary Least squares (OLS)
        -Used in sklean linear regression
    - Gradient Descent
# Algorithm Cheat sheet:

![alt text](https://github.com/harishuideveloper/machine_learning_by_example/blob/master/readme_assets/cheat-sheet.png)