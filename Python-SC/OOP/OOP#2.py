class hero :  #template

    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor

hero1 = hero("strom spirit", 120, 25, 9)
hero2 = hero("teror blade", 200, 35, 7)
hero3 = hero("drow ranger", 130, 40, 12)

print(hero1.armor)
print(hero1.__dict__)
print(hero3.attack, "=", hero3.name)