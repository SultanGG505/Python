class Animal():
    name = ""
    def __init__(self,newName):
        self.name = newName
    def setName(self, newName):
        self.name = newName
    def getName(self):
        print(self.name)


class Dog(Animal):
    def makeNoise(self):
        print(self.name, " говорит Гав")
    def eat(self):
        print(self.name, " скушала корм")

class Cat(Animal):

    def makeNoise(self):
        print(self.name, " говорит мяу")
    def eat(self):
        print(self.name, " скушала мышку")

class Amyoba(Animal):
    def makeNoise(self):
        print(self.name, " Амёбы молчат как бы да.... ")
    def eat(self):
        print(self.name, " скушала планктон")

orangeCat = Cat("Барсик")
orangeCat.setName("Рыжик")
orangeCat.getName()
orangeCat.eat()
orangeCat.makeNoise()

bigDog = Dog("Смешарик")
bigDog.getName()
bigDog.eat()
bigDog.makeNoise()

smallDog = Dog("Смешаричище")
smallDog.getName()
smallDog.eat()
smallDog.makeNoise()

amyobaChad = Amyoba("Chad")
amyobaChad.getName()
amyobaChad.eat()
amyobaChad.makeNoise()

