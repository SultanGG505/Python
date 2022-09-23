def get_key(dict, value):
    for key, values in dict.items():
        if value in values:
            return key

file = open("elements.txt", "r")
strings = file.readlines()
elems = {}

for elem in strings:
    elem = elem.rstrip().split(',')
    elems[elem[0]] = {elem[1], elem[2]}

string = input("Введите число протонов, обозначение или название хим. элемента: ")
while string != "":
    try:
        if string.isdecimal():
            print(elems[string])
        elif not string.isdigit():
            if get_key(elems, string) != None:
                print(get_key(elems, string))
            else:
                raise KeyError
        string = input("Введите число протонов, обозначение или название хим. элемента: ")
    except KeyError:
        print("Такого элемента не существует")
        string = input("Введите число протонов, обозначение или название хим. элемента заново: ")
print("Ввод окончен")
