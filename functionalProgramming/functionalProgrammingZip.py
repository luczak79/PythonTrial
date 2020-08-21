#################################
#  Functional Programming - zip
#################################

my_list = [1,2,3,4,5,6,7,8,9,8]
your_list = [10,20,30,40,50]
name_list = ["Marcin", "Janusz", "Monika"]
zipedd_lists = zip(my_list, your_list, name_list)

print(type(zipedd_lists))
print(list(zipedd_lists))