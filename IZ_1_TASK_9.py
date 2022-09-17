# Задание 9 В файле записана последовательность натуральных чисел.
# Гарантируется, что все числа различны. Рассматриваются всевозможные
# группы
# чисел,
# состоящие
# из
# любого
# количества
# элементов
# последовательности. Необходимо найти наибольшую сумму такой группы,
# заканчивающуюся на 50 Программа должна вывести эту сумму.


# S = [1, 2, 3]
# for m in subsets(S):
#     print(m)

folder = "FilesFor_IZ_1\\"

firstFile = open(folder + "9a.txt", "r")
secondFile = open(folder + "9b.txt", "r")

firstLines = firstFile.readlines()
secondLines = secondFile.readlines()

firstFile.close()
secondFile.close()

# for el in firstLines:
#     el.replace('\n', '')
#
# for el in secondLines:
#     el.replace('\n', '')

readyFirstLines = list(map(str.strip, firstLines))
readySecondLines = list(map(str.strip, secondLines))
firstArr = []
secondArr = []

for el in readyFirstLines:
    firstArr.append(el)
for el in readySecondLines:
    secondArr.append(el)
fArr = list(map(int, firstArr))
sArr = list(map(int, secondArr))

aF = [0] * 100
bF = [0] * 100

for x in fArr:
    a1 = aF.copy()
    for i in range(100):
        if aF[i] != 0:
            a1[(i + x) % 100] = max(a1[(i + x) % 100], aF[i] + x)
    a1[x % 100] = max(a1[x % 100], x)
    aF = a1.copy()

for x in sArr:
    a1 = bF.copy()
    for i in range(100):
        if bF[i] != 0:
            a1[(i + x) % 100] = max(a1[(i + x) % 100], bF[i] + x)
    a1[x % 100] = max(a1[x % 100], x)
    bF = a1.copy()

print(aF[50])
print(bF[50])
