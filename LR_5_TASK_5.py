# . Первое и последнее вхождения. Дана строка. Если в этой
# строке буква f встречается только один раз, выведите её индекс. Если она
# встречается два и более раз, выведите индекс её первого и последнего
# появления. Если буква f в данной строке не встречается, ничего не выводите.
# При решении этой задачи не стоит использовать циклы.

stroka = str(input())

if stroka.count("f") == 1:
    print(stroka.find("f"))
elif stroka.count("f") >= 1:
    print(str(stroka.find("f")) + str(stroka.rfind("f")))
else:
    pass