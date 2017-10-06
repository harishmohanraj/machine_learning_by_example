import re

input_list = []
with open('./dataset.txt','r') as f:
  for line in f:
    input_list.append(line.strip())

N, M = input_list[0].split(" ");

def feature_format(dataset, set_name):
  temp = []
  features, labels = [], []
  if set_name=="train":
    for index, item in enumerate(dataset):
      labels.append(item.split(" ")[1])
      item_feature = item.split(" ")[2:]
      features.append([re.sub(r"^(.*?):", "", y) for y in item_feature])
    for index, list_item in enumerate(features):
      for pos, item in enumerate(list_item):
        features[index][pos] = float(item)
    return features, labels
  else:
    for index, item in enumerate(dataset):
      item = item.split(" ")[1:]
      features.append([re.sub(r"^(.*?):", "", y) for y in item])
    for index, list_item in enumerate(features):
      for pos, item in enumerate(list_item):
        features[index][pos] = float(item)
    return features

training_features, training_labels = feature_format(input_list[1:int(N)+1], 'train')
testing_features = feature_format(input_list[int(N)+1:][1:], 'test')



from sklearn.tree import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(training_features, training_labels)
pred = clf.predict(testing_features)


for i, j in enumerate(input_list[int(N)+1:][1:]):
  print(j.split(" ")[0]+" "+ pred[i])