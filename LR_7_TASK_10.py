# Переставить min и max. В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка
a = []
for i in range(int(input())):
    a.append(int(input()))

min_a = a.index(min(a))
max_a = a.index(max(a))
a[min_a], a[max_a] = a[max_a], a[min_a]

# a[a.index(min(a))], a[a.index(max(a))] = a[a.index(max(a))], a[a.index(min(a))] почему так не заработало?(((

for elem in a:
    print(elem, sep=", ")
