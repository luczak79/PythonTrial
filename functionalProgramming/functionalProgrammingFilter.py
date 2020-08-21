#################################
#  Functional Programming - filter
#################################

def only_odd(item):
  return item % 2 != 0

filter_list = [1,2,3,4,5,6,7,8,9]
result = filter(only_odd, filter_list)

print(type(result))
print(list(result))
print(filter_list)