"""
In this example we are using sklearn(http://scikit-learn.org/stable/index.html)python library.
The below example illustrates the supervised learning methods based on applying Bayes’
theorem(Gaussian Naive Bayes) with strong (naive) feature independence assumptions.

In the below code snippet we are passing the features(X) and the expected output(Y)
to the classifier function to train our modal to predict the labels
              Features ---> | modal | ---> labels
And finally we pass a test data set to the classifier function which predicts the output
based on the training dataset(dataset used to train our modal).

"""
### import the numPy module as np
import numpy as np
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))
print(clf.predict([[0.8, 1]]))