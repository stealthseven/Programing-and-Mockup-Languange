class hero :  #template
    pass 

hero1 = hero()  #object
hero2 = hero()
hero3 = hero()

hero1.name = "sniper"
hero1.attack = "30"
hero1.health = "100"

hero2.name = "axe"
hero2.attack = "10"
hero2.health = "500"

hero3.name = "void spirit"
hero3.attack = "25"
hero3.health = "250"


print(hero1.__dict__)
print(hero1)
print(hero1.name)