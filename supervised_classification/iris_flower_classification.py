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
#importing decision tree classifier from sklearn
from sklearn import tree

iris = load_iris()
# starting index of each flower
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#training the decision tree classifier by passing the training data
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
#importing graphviz for data visualization
import graphviz
#Code for creating the decision tree graph
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
#Exporting the graph into a pdf document
graph = graphviz.Source(dot_data)
graph.render("iris")