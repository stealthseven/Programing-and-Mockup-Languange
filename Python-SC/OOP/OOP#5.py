# game sederhana "saling serang dan bertahan"
# -OOP#5-


class hero:
    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.name)
        attack_diterima = attackPower_lawan/self.armor
        print("serangan terasa :" + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " tersisa " + str(self.health))


phantomAssasin = hero("phantomAssasin", 100, 25, 6)
darkSheer = hero("darkSheer", 125, 10, 7)

phantomAssasin.serang(darkSheer)
print("\n")
darkSheer.serang(phantomAssasin)

print(dict(phantomAssasin))
