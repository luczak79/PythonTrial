#################################
#  MRO - method resolution order
#################################


class A:
  num = 10

class C(A):
  num = 1

class B(A):
  num = 99

class D(C, B):
  pass

print(D.num)
