class StringVar():
    text = ""

    def __init__(self, newText):
        self.text = newText

    def set(self, newText):
        self.text = newText

    def get(self):
        return self.text

myString = StringVar("Сегодня 25 сентября")

print(myString.get())
print("Но ведь это не так! Поменяйте дату!")
myString.set(input("Вводите дату!\n"))
print(myString.get())