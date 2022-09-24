import tkinter
from tkinter import filedialog
from tkinter import *

# Задание 3*. Напишите программу, которая позволяет произвольный
# текст, введенный с клавиатуры, по нажатию кнопки сохранить в обычный
# текстовый файл либо в файл HTML-формата (тип файла указывается с
# помощью выпадающего меню).

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


def savefileastxt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write(entry_1.get())
        f.close()


def savefileashtml():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        # html_template1.replace("Title", path)
        f.write(html_template1)
        f.write(entry_1.get())
        f.write(html_template2)
        f.close()


window = tkinter.Tk()

window.title('Notepad')
window.geometry('800x800')

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save as txt", command=savefileastxt)
filemenu.add_command(label="Save as html", command=savefileashtml)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

entry_1 = Entry(width=100, borderwidth=2, relief="solid")
entry_1.grid(row=0, column=1, pady=10, padx=10)
exet = Button(window, text='Выйти из программы', command=window.destroy)
exet.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

window.config(menu=menubar)
window.config(bg="gray50")
window.mainloop()
