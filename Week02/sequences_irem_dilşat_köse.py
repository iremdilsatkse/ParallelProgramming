my_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]

my_tuple =(4, 7, "Parallel", "Programming")

my_set = {"Python", "Bora", "Canbula"}

my_dic = {"Name": "İrem", "Age": "22", "job": "student"}

def remove_duplicates(my_list):
  new_list = list(set(my_list))
  return new_list

def list_counts(my_list):
  count = {}
  for i in my_list:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  return count

def reverse_dict(my_dict):
  reversed_dict = {v: key for key, v in my_dict.items()}
  return reversed_dict
