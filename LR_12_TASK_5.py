# Задание 5. Самое длинное слово в файле. В данном задании вы должны
# написать программу, которая будет находить самое длинное слово в файле. В
# качестве результата программа должна выводить на экран длину самого
# длинного слова и все слова такой длины. Для простоты принимайте за
# значимые буквы любые непробельные символы, включая цифры и знаки
# препинания.

fname = input("Введите название файла для чтения: ") + ".txt"

is_file_opened = False
while is_file_opened == False:
    try:
        inp = open(fname, "r")
        is_file_opened = True
    except FileNotFoundError:
        fname = input("Файл не найден. Введите название файла заново: ") + ".txt"

words = ''
strings = inp.readlines()
for str in strings:
    if str != "\n":
        words += str.rstrip() + " "
inp.close()

words = words.split()
max = len(words[0])
for word in words:
    if len(word) > max:
        max = len(word)

out = open("lr_12_5_output.txt", "w")
out.write(f"Длина самого длинного слова - {max}\n")
for word in words:
    if len(word) == max:
        out.write(word + '\n')
out.close()