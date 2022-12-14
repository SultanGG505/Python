# Снежинка. Дано нечетное число 𝑛. Создайте двумерный
# массив из 𝑛 × 𝑛 элементов, заполнив его символами «.» (каждый элемент
# массива является строкой из одного символа). Затем заполните символами «*»
# среднюю строку массива, средний столбец массива, главную диагональ и
# побочную диагональ. В результате единицы в массиве должны образовывать
# изображение звездочки. Выведите полученный массив на экран, разделяя
# элементы массива пробелами.
n = int(input())
# list = [ x ** 2 if x % 2 else x for x in range (1, 101)]
a = [[0] * n for i in range(n)]

for i in range(n):
    a[i][i] = 1
    a[i][n - i - 1] = 1
    a[(n // 2)][i] = 1
    a[i][(n // 2)] = 1
for row in a:
    print(' '.join(["*" if elem == 1 else "." for elem in row]))
