class Animal(object):

    name = "Not named"
    def __init__(self) -> object:
        print("Animal constructed")


class Mammal(Animal):
    hasHair = True

    def __init__(self):
        print("Mammal constructed")

class Reptile(Animal):
    hasScales = True
    def __init__(self):
        print("Reptile constructed")

class Dragon(Mammal, Reptile):
    hasWings = True
    
    def __init__(self):
        super(Dragon.self).__init__()
        print("Dragon constructed")

    def __del__(self):
        print(self.__class__.__name__ + " destroyed")


myAnimal = Animal()
Animal.name = "butt"
elyse = Animal()
print(elyse.name)

print("start")
myDragon = Dragon()
myDragon.name = "sam"
print("finished")












