#################################
#  Functional Programming - lambda expressions
#################################

from functools import reduce

moja_lista = [1,2,3,4,5]

def accumulator(acc, item):
  return acc + item

def only_odd(item):
  return item % 2 != 0

def multiply_by2(item):
  return item * 2

print(list(map(multiply_by2, moja_lista)))
print(list(map(lambda item: item*2, moja_lista)))

print(list(filter(lambda item: item % 2 !=0, moja_lista)))
print(reduce(lambda acc, item: acc + item, moja_lista))

print(list(map(lambda item: item*item, moja_lista)))

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)
