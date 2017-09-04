"""
Iris is a classical machine learning problem. In it you have to identify
the what type of flower you have based on different measurements like the
length and width of the petal.

The dataset includes 3 different types of flower and they are all
species of Iris
  1) Setosa
  2) versicolor
  3) virginica

The data set has 50 examples of each species. There are 4 features
to identify the type of flower
  1) Sepal Length (cm)
  2) Sepal width (cm)
  3) Petal length (cm)
  4) Petal width (cm)

Our goal is to use this dataset to train a classifier,
then we can use the classifier to predict what species
of flower we have if we were given a new flower we have
never seen before
"""
#importing the iris dataset from sklearn library
from sklearn.datasets import load_iris
#importing numpy library
import numpy as np

iris = load_iris()
# starting index of each flower
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)