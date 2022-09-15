# Имена без повторов. Продолжаем использовать базу имен из
# задания 15 Проходя по файлам, выберите имена без дублирования отдельно
# для мальчиков и для девочек и выведите их на экран. Разумеется,
# повторяющихся имен в этих списках быть не должно.

# aboba = 1900
# int = open("Names\\" + str(aboba) + "_BoysNames.txt", "r")
# print("ok")

# a = set()
# words = ['hello', 'daddy', 'hello', 'mum']
# set(words)
# print(set(words))

# 1900-2012

folder = "Names\\"
IterBoy = "_BoysNames.txt"
IterGirl = "_GirlsNames.txt"

IBOY = 1900
IGIRL = 1900

ResBoy = set()
ResGirl = set()

while IBOY != 2013:
    file = open(folder + str(IBOY) + IterBoy, "r")
    lines = file.readlines()
    for line in lines:
        Lst = line.split()
        ResBoy.add(Lst[0])
    file.close()
    IBOY += 1

while IGIRL != 2013:
    file = open(folder + str(IGIRL) + IterGirl, "r")
    lines = file.readlines()
    for line in lines:
        Lst = line.split()
        ResGirl.add(Lst[0])
    file.close()
    IGIRL += 1

# print("Уникальные имена мальчиков с 1900 по 2012:")
# for el in ResBoy:
#     print(el, sep=", ")
#
# print(""
#       ""
#       ""
#       ""
#       ""
#       "")
#
# print("Уникальные имена девочек с 1900 по 2012:")
# for el in ResGirl:
#     print(el, sep=", ")


ResFileBoy = open(folder + "ResBoy.txt", "w")
for el in ResBoy:
    ResFileBoy.write(el + "\t\n")
ResFileBoy.close()

ResFileGirl = open(folder + "ResGirl.txt", "w")
for el in ResGirl:
    ResFileGirl.write(el + "\t\n")
ResFileGirl.close()
