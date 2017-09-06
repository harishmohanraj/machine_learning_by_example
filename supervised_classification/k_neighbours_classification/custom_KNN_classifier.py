"""
This example is the minimal custom implementation of k_neighbours classification.

The k-NN algorithm is among the simplest of all machine learning algorithms.
K nearest neighbors algorithm stores all available cases (training data)
and classifies new cases (testing data) based on a similarity measure
(e.g., distance functions).

"""

# importing the iris dataset from sklearn library
from sklearn.datasets import load_iris
# importing scipy package to find the distance between
# two points using Euclidean Distance
from scipy.spatial import distance
# Function to return the euclidean distance between
# two points
def euc(a, b):
  # a - is the point from training data
  # b - is the point from testing data
  return distance.euclidean(a, b)

# Custom implementation of KNeighbours classification
class MinimalKNN():
  # Fit method to feed the training date to the classifier
  def fit(self, X_train, y_train):
    # Assigning training data and training labels
    # in local variables
    self.X_train = X_train
    self.y_train = y_train

  # Passing the testing data to the predict function to return
  # the label based on the nearest training data
  def predict(self, X_test):
    predictions = []
    # Our testing data is a 2 dimentional array - [[], [], []]
    # So we have to loop through the testinf data and find the
    # closest matching training data point for each testing data
    # point
    for row in X_test:
      # Passing each row to the closestv function
      # which returns the closest label
      label = self.closest(row)
      predictions.append(label)
    return predictions

  # The closest function will loop through the training data
  # and tries to find the closest matching point for the given
  # testing data and returns the label for the closest matching
  # training data
  def closest(self, row):
    # row is the testing data
    # X_train is the training data
    # best_dist is assigned to the first value of the training data
    best_dist = euc(row, self.X_train[0])
    best_index = 0
    # Looping through the training data to find any other closest
    # matching point for our testing data. If a closest possible
    # match is found then reassign the best_dist and best_index
    # to the matched training data and finally return the training
    # lable for the corresponding training data point
    for i in range(1, len(self.X_train)):
      dist = euc(row, self.X_train[i])
      if dist < best_dist:
        best_dist = dist
        best_index = i
    return self.y_train[best_index]

# Loading the iris data set
iris = load_iris()
# assigning the data and the label to X and y
# f(X) = y
X = iris.data
y = iris.target

# importing the test training spliting module from sklearn library
from sklearn.cross_validation import train_test_split
# X_train - training dataset
# X_test - testing dataset
# y_train - training labels
# y_test - testing labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# importing custom MinimalKNN classifier from the above class
clf = MinimalKNN();
clf.fit(X_train, y_train);
predictions = clf.predict(X_test)

# importing accuracy_score module from sklearn to test the
#accuracy of our classifier
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(predictions, y_test)
print(accuracy)