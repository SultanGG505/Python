class Animal():
    name = ""

    def eat(self):
        print("Намнём")
        print(self.name," покушал(а)")

    def __init__(self, newName):
        self.name = newName
        print("Родилось животное ", self.name)

    def set_name(self, newName):
        self.name = newName

    def get_name(self):
        return self.name

    def makeNoise(self):
        print(self.name, " говорит Гррр")


dog = Animal("Рекс")
print("Имя собаки -> ", dog.get_name())
print("Поменяем собаке имя, почему бы и нет? Введите его!")
dog.set_name(input())
dog.eat()
dog.makeNoise()
