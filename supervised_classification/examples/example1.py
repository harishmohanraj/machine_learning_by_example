input_list = []
with open('./dataset2.txt','r') as f:
  for line in f:
    input_list.append(line.strip())

testcases = input_list[0];
list_without_testcase = input_list[1:]
list_of_test_data = [list_without_testcase[x:x+7] for x in range(0, len(list_without_testcase), 7)]

def sort_and_return_index(list):
  student_dict = {}
  for index, item in enumerate(list):
    student_dict[item] = index+1
  return [value for (key, value) in sorted(student_dict.items(), reverse=True)]

def get_sorted_test_list(list_item):
  sorted_test_list = [];
  for item in list_item:
    splitted_list = item.split(" ")
    sorted_test_list.append(sort_and_return_index(list(map(float, splitted_list))))
  return sorted_test_list

def sort_and_return_length(gpa_sorted_by_rank, test_rank):
  return len([i for i, j in zip(gpa_sorted_by_rank, test_rank) if i == j])

def get_most_relevalt_test(gpa_sorted_by_rank, aptitude_tests_sorted_by_rank):
  most_relevant_test = []
  for test_rank in aptitude_tests_sorted_by_rank:
    most_relevant_test.append(sort_and_return_length(gpa_sorted_by_rank, test_rank))
  return most_relevant_test

def best_aptitude_test_finder():
  gpa_sorted_by_rank = sort_and_return_index(gpa)
  aptitude_tests_sorted_by_rank = get_sorted_test_list(preformance_of_aptitude_tests)
  relevant_apptitude_test = get_most_relevalt_test(gpa_sorted_by_rank, aptitude_tests_sorted_by_rank)
  return relevant_apptitude_test.index(max(relevant_apptitude_test))+1

for index, item in enumerate(list_of_test_data):
  #number_of_admitted_students = item[1];
  gpa = item[1].split(" ")
  preformance_of_aptitude_tests = item[2:]
  print(best_aptitude_test_finder());
  #print(item[2:])