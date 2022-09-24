import tkinter
from tkinter import filedialog
from tkinter import *
from math import pi

# Задание 5. Посчитать объём сферы по радиусу и сохранить в файл

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""


# <p>Default code has been loaded into the Editor.</p>

def click():
    # Получаем строковое содержимое поля ввода с помощью метода get()
    # C помощью config() можем изменить отображаемый текст

    if entry_1.get().isdigit():
        inp = float(entry_1.get())
        try:
            res = (4 * pi * inp ** 3) / 3
            label_3.config(text=res)
        except:
            label_3.config(text="Ошибка, введите число!")
    else:
        label_3.config(text="Ошибка, введите число!")


def savefileastxt():
    var = str(label_3.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
            window.title('Notepad - ' + path + ".txt")
        except:
            return
        with open(path + ".txt", 'w') as f:
            f.write("Ответ для радиуса длины " + str(entry_1.get()) + " = " + str(label_3.cget("text")))
            f.close()
    else:
        pass


def savefileashtml():
    var = str(label_3.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
            window.title('Notepad - ' + path + ".html")
        except:
            return
        with open(path + ".html", 'w') as f:
            # html_template1.replace("Title", path)
            f.write(html_template1)
            f.write("Ответ для радиуса длины " + str(entry_1.get()) + " = " + str(label_3.cget("text")))
            f.write(html_template2)
            f.close()
    else:
        pass


window = tkinter.Tk()
window.title("Перевод Фаренгейт в градусы")

window.config(bg="black")

label_1 = Label(text="Ввод ->", width=30, borderwidth=2, relief="solid")
label_1.grid(row=0, column=0, pady=10, padx=10)

label_2 = Label(text="Ответ ->", width=30, borderwidth=2, relief="solid")
label_2.grid(row=3, column=0, pady=10, padx=10)

label_3 = Label(width=30, borderwidth=2, relief="solid")
label_3.grid(row=3, column=1, pady=10, padx=10)

entry_1 = Entry(width=30, borderwidth=2, relief="solid")
entry_1.grid(row=0, column=1, pady=10, padx=10)

button_1 = Button(text="Посчитать", width=30, command=lambda: click())
button_1.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

button_2 = Button(text="Сохранить в .txt", width=15, command=lambda: savefileastxt())
button_2.grid(row=4, column=0, columnspan=1, pady=10, padx=10)

button_3 = Button(text="Сохранить в .html", width=15, command=lambda: savefileashtml())
button_3.grid(row=4, column=1, columnspan=1, pady=10, padx=10)

exet = Button(window, text='Выйти из программы', command=window.destroy)
exet.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

window.mainloop()
