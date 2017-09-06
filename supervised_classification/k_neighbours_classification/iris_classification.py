# importing the iris dataset from sklearn library
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

# importing the test training spliting module from sklearn library
from sklearn.cross_validation import train_test_split
# X_train - training dataset
# X_test - testing dataset
# y_train - training labels
# y_test - testing labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# importing decision tree classifier from sklearn
# from sklearn import tree
# clf = tree.DecisionTreeClassifier();

# importing decision tree classifier from sklearn
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier();
clf.fit(X_train, y_train);
predictions = clf.predict(X_test)

# importing accuracy_score module from sklearn to test the
#accuracy of our classifier
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(predictions, y_test)

print(accuracy)