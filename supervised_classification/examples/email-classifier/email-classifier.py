input_list = []
with open('./trainingdata.txt','r') as f:
  for line in f:
    input_list.append(line.strip())
print(input_list)