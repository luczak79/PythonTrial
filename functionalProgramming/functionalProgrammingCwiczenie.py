#################################
#  Functional Programming - excercise
#################################

my_list = []
my_list = [char for char in 'hello']
my_list2 = [num for num in range(1,101)]
my_list3 = [num*2 for num in range(1,101)]
my_list4 = [num for num in range(1,101) if num%2 == 0]
print(my_list4)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']

duplicates = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates)