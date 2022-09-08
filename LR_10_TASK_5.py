#  Кубики. Аня и Боря любят играть в разноцветные кубики,
# причем у каждого из них свой набор и в каждом наборе все кубики различны
# по цвету. Однажды дети заинтересовались, сколько существуют цветов таких,
# что кубики каждого цвета присутствуют в обоих наборах. Для этого они
# занумеровали все цвета случайными числами от 0 до 108
# . На этом их
# энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
# В первой строке входных данных записаны числа 𝑁 и 𝑀 – число кубиков
# у Ани и Бори. В следующих 𝑁 строках заданы номера цветов кубиков Ани. В
# последних 𝑀 строках номера цветов Бори.
# 6
# Найдите три множества: номера цветов кубиков, которые есть в обоих
# наборах; номера цветов кубиков, которые есть только у Ани и номера цветов
# кубиков, которые есть только у Бори. Для каждого из множеств выведите
# сначала количество элементов в нем, а затем сами элементы, отсортированные
# по возрастанию.
# Входные данные
# 4 3
# 0
# 1
# 10
# 9
# 1
# 3
# 0
# Правильный ответ
# 2
# 0 1
# 2
# 9 10
# 1
# 3


n, m = int(input("Введите N ")), int(input("Введите M "))
A = set()
B = set()

Both = set()
Both_sps = []
OnlyAnya = set()
OnlyAnya_sps = []
OnlyBorya = set()
OnlyBorya_sps = []

for i in range(n):
    tmp = int(input("Введите номер кубика Ани "))
    A.add(tmp)

for i in range(m):
    tmp = int(input("Введите номер кубика Бори "))
    B.add(tmp)


Both = A.intersection(B)
for elem in Both:
    Both_sps.append(elem)
Both_sps.sort()

OnlyAnya = A.difference(B)
for elem in OnlyAnya:
    OnlyAnya_sps.append(elem)
OnlyAnya_sps.sort()

OnlyBorya = B.difference(A)
for elem in OnlyBorya:
    OnlyBorya_sps.append(elem)
OnlyBorya_sps.sort()

print("Кол-во эл-ов об-ия равно = " + str(len(Both)))
for elem in Both_sps:
    print(elem)

print("Кол-во эл-ов уникальных кубиков Ани = " + str(len(OnlyAnya_sps)))
for elem in OnlyAnya_sps:
    print(elem)

print("Кол-во эл-ов уникальных кубиков Бори = " + str(len(OnlyBorya_sps)))
for elem in OnlyBorya_sps:
    print(elem)


