# print(1, 2, 3)
# print(1, 2, 3, sep=', ', end='. ')

# Даны два целых числа 𝐴 и 𝐵 (при этом 𝐴 ≤ 𝐵).
# Выведите все числа от 𝐴 до 𝐵 включительно.

print("введите A и B")

a = int(input())
b = int(input())

for i in range(a, b+1):
    print(i)
