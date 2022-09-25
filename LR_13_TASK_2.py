class Animal():
    name = ""

    def eat(self):
        print("Намнём")

    def __init__(self, newName):
        self.name = newName
        print("Родилось животное ", self.name)

    def set_name(self, newName):
        self.name = newName

    def get_name(self):
        return self.name

    def makeNoise(self):
        print(self.name, " говорит Гррр")


dog = Animal("aboba")
dog.makeNoise()
