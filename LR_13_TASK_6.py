class Animal():
    def __init__(self):
        print("Родилось животное")


class Dog(Animal):
    name = ""

    def __init__(self, newName = ""):
        self.name = newName
        print("Родилась собака ", self.name)
        Animal.__init__(self)

    def makeNoise(self):
        print(self.name, " говорит Гав")


noNameDog = Dog()
Reks = Dog("Reks")
Reks.makeNoise()