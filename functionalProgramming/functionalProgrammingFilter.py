#################################
#  Functional Programming - filter
#################################

class Czlowiek():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return 'Name: {self.name}, Age: {self.age}'.format(self=self)

def only_odd(item):
  return item % 2 != 0

def moreThanFive(number):
  if number > 5:
    return True
  else:
    return False

def tylkoPelnoletni(uczestnik):
  if uczestnik.age > 18:
    return True
  else:
    return False

listaUczestnikowWycieczki = []
listaUczestnikowWycieczki.append(Czlowiek("Marcin", 41))
listaUczestnikowWycieczki.append(Czlowiek("Janek", 43))
listaUczestnikowWycieczki.append(Czlowiek("Julka", 17))
listaUczestnikowWycieczki.append(Czlowiek("Tomek", 33))
listaUczestnikowWycieczki.append(Czlowiek("Ewelina", 16))

filter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = filter(only_odd, filter_list)
result2 = filter(moreThanFive, filter_list)
pelnoletni = list(filter(tylkoPelnoletni, listaUczestnikowWycieczki))

print('orginalna lista:',filter_list)
print('nieparzyste:',list(result1))
print('wieksze niż 5:',list(result2))

print('Pelnoletni uczestnicy wycieczki:')
for x in pelnoletni:
  print(x.__str__())
