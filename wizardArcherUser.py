############################
#  Wizard, Archer, User
############################

class User():
  def sign_in(self):
    print("Uzytkownik wlasnie sie zalogował")

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Atak Czarownika: {self.power} mocy')

class Archer(User):

  num_arrows = 0

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
    print(f'Łucznik {self.name} wchodzi do gry. Ilość strzał {self.num_arrows}.')

  def attack(self):
    self.num_arrows = self.num_arrows - 1
    print(f'Atak łucznika {self.name}. Pozostało {self.num_arrows} strzał."')

  def run(self):
    print('Biegnie bardzo szybko.')


class HybridBorg(Archer, Wizard):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)

hybryda = HybridBorg("JanuszHybryda", 60, 100)
hybryda.attack()

hybryda2 = HybridBorg("GrazynaHybryda", 50, 100)
hybryda2.attack()

wizard1 = Wizard("Merlin", 60)
wizard2 = Wizard("Harry Potter", 20)
archer1 = Archer("Thorgal", 20)
archer2 = Archer("Robin Hood", 20)

users = [archer1, wizard2, archer2, wizard1]

print(dir(wizard1))