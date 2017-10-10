import csv
import numpy as np

with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    data_list = list(reader)

data_list = data_list[1:]

# cleaning the dataset by removing the special characters
for i in data_list:
  i[0] = i[0].replace('\xe6',' ')
  i[0] = i[0].replace('\xa3',' ')
  i[0] = i[0].replace('\xcd',' ')
  i[0] = i[0].replace('\xf3',' ')
  i[0] = i[0].replace('\xf1',' ')
  i[0] = i[0].replace('\xbb',' ')
  i[0] = i[0].replace('\r',' ')
  i[1] = i[1].replace('\xe6',' ')
  i[1] = i[1].replace('\xa3',' ')
  i[1] = i[1].replace('\xcd',' ')
  i[1] = i[1].replace('\xf3',' ')
  i[1] = i[1].replace('\xf1',' ')
  i[1] = i[1].replace('\xbb',' ')
  i[1] = i[1].replace('\r',' ')

# Extracting the features and labels from the dataset
features_list = []
labels_list = []
for index, item in enumerate(data_list):
  features_list.append(item[:2])
  labels_list.append(item[2:])

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features_list, labels_list, test_size=0.30, random_state=42)

# converting 2d list into 1d list
features_train = np.array(sum(features_train, []))
features_test = np.array(sum(features_test, []))

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
features_train_extracted = vectorizer.fit_transform(features_train)

features_train_extracted = features_train_extracted.todense()

print features_train_extracted.shape
print len(labels_train)

#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()
#clf.fit(features_train_extracted, labels_train)
#predictions = clf.predict(features_test)

#from sklearn.metrics import accuracy_score
#acc = accuracy_score(predicted, labels_test)
#print acc


