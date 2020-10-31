class Hero:  # template
    # class variablE
    Jumlah = 0

    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        # instance Variable
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.Jumlah += 1

    # void Function//method tanpa return//tanpa argumen
    def siapa(self):
        print("namaku adalah" + self.name)

    # method dengan argumen//tanpa return
    def healthUp(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("earth spirit", 200, 30, 10)
hero2 = Hero("invoker", 95, 50, 5)

hero1.siapa()
hero1.healthUp(20)

print(hero1.getHealth())
