### import the sklearn module for tree
from sklearn import tree
### import the numpy
import numpy as np
### Define the features and labels to train our classifier
features=np.array([[140, 'smooth'],[130, 'smooth'],[150, 'bumpy'],[170, 'bumpy'],[100, 'smooth'], [200, 'bumpy']]);
labels=np.array(["apple", "apple", "orange", "orange", "apple", "orange"]);
### Converting the classifier into boolean dor mimplicity sake.
features_in_binary = np.array([[140, 0],[130, 0],[150, 1],[170, 1],[100, 0], [200, 1]]);
labels_in_binary=np.array([0, 0, 1, 1, 0, 1]);

### Define the features and labels to train our classifier
testing_features = np.array([[10, 0],[1220, 0],[140, 1],[70, 0],[10, 1], [230, 1]]);
testing_labels=np.array([0, 1, 1, 0, 0, 1]);
### create a classifier by instanciating the constructor function
clf = tree.DecisionTreeClassifier()
### Train our classifier with training data,fit => find patterns in data
clf.fit(features_in_binary, labels_in_binary)
### import the sklearn module for accuracy_score to predict the accuracy of our classifier
from sklearn.metrics import accuracy_score
### Predict the accuracy of our training data by passing testing data

print("Orange" if clf.predict([[190, 1]]) == [1] else "Apple")
print("Orange" if clf.predict([[10, 0]]) == [1] else "Apple")
print("Orange" if clf.predict([[1190, 0]]) == [1] else "Apple")
