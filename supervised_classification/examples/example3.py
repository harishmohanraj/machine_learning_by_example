import csv
with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    data_list = list(reader)

data_list = data_list[1:]

features_list = []
labels_list = []
for index, item in enumerate(data_list):
  features_list.append(item[:2])
  labels_list.append(item[2:])
