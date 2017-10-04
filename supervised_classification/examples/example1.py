
lines = []
with open('./dataset.txt','r') as f:
  for line in f:
    lines.append(line.strip())

testcases = lines[0];
number_of_admitted_students = lines[1];
gpa = lines[2].split(" ")
preformance_of_aptitude_tests = lines[3:]

def sort_and_return_index(list):
  student_dict = {}
  for index, item in enumerate(list):
    student_dict[item] = index+1
  return [value for (key, value) in sorted(student_dict.items(), reverse=True)]

def get_sorted_test_list(list_item):
  res = [];
  for item in range(len(list_item)):
    #res.append(sort_and_return_index(list_item[item])
    #list(map(int, splitted_list))
    splitted_list = list_item[item].split(" ")
    res.append(sort_and_return_index(list(map(int, splitted_list))))
  return res

gpa_sorted_by_rank = sort_and_return_index(gpa)
aptitude_tests_sorted_by_rank = get_sorted_test_list(preformance_of_aptitude_tests)

def get_most_relevalt_test(gpa_sorted_by_rank, aptitude_tests_sorted_by_rank):
  result_len = []
  for test_rank in aptitude_tests_sorted_by_rank:
    print([i for i, j in zip(gpa_sorted_by_rank, test_rank) if i == j])
    result_len.append(len(set(gpa_sorted_by_rank) & set(test_rank)))
  return result_len

relevant_apptitude_test = get_most_relevalt_test(gpa_sorted_by_rank, aptitude_tests_sorted_by_rank)