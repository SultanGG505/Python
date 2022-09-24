# master = Tk()
# master.title("Python")
#
# def close(event):
#     sys.exit()
#
# master.bind('<Escape>',close)
# master.mainloop()

# from Tkinter import *
# #use tkinter instead of Tkinter (small, not capital T) if it doesn't work
# #as it was changed to tkinter in newer Python versions
#
# root = Tk()
# Button(root, text="Quit", command=root.destroy).pack() #button to close the window
# root.mainloop()


# Задание 1. Напишите программу, переводящую градусы по Фаренгейту
# в градусы по Цельсию. Интерфейс работы с программой представлен ниже.

import tkinter


# Вызывается в момент нажатия на кнопку:
def click():
    # Получаем строковое содержимое поля ввода с помощью метода get()
    # C помощью config() можем изменить отображаемый текст
    faren = entry.get()
    # (Фаренгейт — 32): 1, 8 = Цельсий
    try:
        res = (float(faren) - 32) / 1.8
        label.config(text=res)
    except:
        label.config(text="Ошибка, введите число!")
        ValueError

window = tkinter.Tk()
window.title("Перевод Фаренгейт в градусы")
window.geometry('350x450+700+200')
frame = tkinter.Frame(window)
frame.pack(side='top')
entry = tkinter.Entry(frame)
entry.pack(side='top')
label = tkinter.Label(frame)
label.pack(side='top')
# Привязываем обработчик нажатия на кнопку к функции click()
button = tkinter.Button(frame, text='Посчитать градусы в цельсиях!', command=click)
button.pack(side='top')
exet = tkinter.Button(window, text='Выйти из программы', command=window.destroy).pack(side='top')
window.mainloop()
