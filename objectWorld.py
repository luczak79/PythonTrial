class PlayerCharacter:

    membership = True
    taka_sobie_lista = []

    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age
            self.taka_sobie = []

    def run(self):
        print(self.name + ':run')

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def born_kid(cls, pl1, pl2):
        return cls(f'I am a kid of {pl1.name} and {pl2.name}', 0)

    @staticmethod
    def adding_age_static(pl1, pl2):
        return pl1.age + pl2.age

player1 = PlayerCharacter("Marcin Luczak", 33)
player2 = PlayerCharacter("Jim Morrison", 44)

print(PlayerCharacter.adding_age_static(player1, player2))
player3 = PlayerCharacter.born_kid(player1, player2)
print("Player3: " + player3.name)

player1.shout()
player2.shout()



