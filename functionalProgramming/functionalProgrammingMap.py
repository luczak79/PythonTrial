#################################
#  Functional Programming - map
#################################

def multiply_by2(item):
  return item * 2


my_list = [1,2,3]
new_list = map(multiply_by2, my_list)

print(type(new_list))
print(list(new_list))
print(my_list)