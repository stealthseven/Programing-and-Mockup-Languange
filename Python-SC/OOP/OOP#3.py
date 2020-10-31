class Hero : #template
    
    Jumlah = 0 #class variablE
    
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.name = inputName       # instance Variable 
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.Jumlah += 1
        print("membuat karakter dengan nama" + inputName)

hero1 = Hero("strom spirit", 120, 25, 9)
print(Hero.Jumlah)
hero2 = Hero("teror blade", 200, 35, 7)
print(Hero.Jumlah)
hero3 = Hero("drow ranger", 130, 40, 12)
print(Hero.Jumlah)

