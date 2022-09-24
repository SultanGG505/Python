# Задание 2. Напишите программу, которая отображает случайное слово
# на русском языке (тип данных dict). Пользователь пытается угадать его на
# английском (или другом языке). Дополнительно ограничить работу
# программы по числу неправильно угаданных слов.

from tkinter import *
import tkinter


# # Вызывается в момент нажатия на кнопку:
# def click():
#     Получаем строковое содержимое поля ввода с помощью метода get()
#     C помощью config() можем изменить отображаемый текст
#
#     label.config(text="res")


window = tkinter.Tk()
window.title("Угадай слово")

dictionary = {"яблоко": "apple",
              "абрикос": "apricot",
              "апельсин": "orange",
              "груша": "pear",
              "лайм": "lime",
              "мандарин": "tangerine",
              "персик": "peach",
              "дыня": "melon",
              "лимон": "lemon",
              "папайя": "papaya",
              }

# capital, country = random.choice(list(d.items()))

Label(text="random word ->", width=30, borderwidth=2, relief="solid").grid(row=0, column=0, pady=10, padx=10)
Label(width=30, borderwidth=2, relief="groove").grid(row=0, column=1, pady=10, padx=10)
Button(text="зарандомить", width=30).grid(row=1, column=0, columnspan=3, pady=10, padx=10)

exet = tkinter.Button(window, text='Выйти из программы', command=window.destroy)
window.mainloop()
