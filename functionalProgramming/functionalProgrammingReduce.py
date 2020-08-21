#################################
#  Functional Programming - reduce
#################################

from functools import reduce

moja_lista = [1,2,3,4,5]

def accumulator(acc, item):
  return acc + item

print(reduce(accumulator, moja_lista, 0))