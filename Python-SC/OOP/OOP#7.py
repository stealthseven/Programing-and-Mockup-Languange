class hero :
    #class variable
    jumalah = 0 

    def __init__(self,name,health):
        self.name = name 
        self.health = health

        #variable instance private
        self.__private = "private"
        #variable instance protected
        self._protected = "protected"

lina = hero("lina",100)

print(lina.__dict__)
print(lina._protected)
lina._protected = "testing"
print(lina.__dict__)
print(lina._protected)