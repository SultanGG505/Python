import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
var = tkinter.StringVar()
# Обновление содержимого переменной происходит в режиме реального времени
label = tkinter.Label(frame, textvariable=var)
label.pack()
# Пробуем набрать текст в появившемся поле для ввода
6
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()
