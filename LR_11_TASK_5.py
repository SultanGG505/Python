# Права доступа. В файловую систему одного
# суперкомпьютера проник вирус, который сломал контроль за правами доступа
# к файлам. Для каждого файла известно, с какими действиями можно к нему
# обращаться:
# 1) запись W;
# 2) чтение R;
# 3) запуск X.
# В первой строке содержится число 𝑁 – количество файлов
# содержащихся в данной файловой системе. В следующих 𝑁 строчках
# содержатся имена файлов и допустимых с ними операций, разделенные
# пробелами. Далее указано число 𝑀 – количество запросов к файлам. В
# последних 𝑀 строках указан запрос вида Операция Файл. К одному и тому же
# файлу может быть применено любое количество запросов.
# Вам требуется восстановить контроль над правами доступа к файлам
# (ваша программа для каждого запроса должна будет возвращать OK если над
# файлом выполняется допустимая операция, или же Access denied, если
# операция недопустима.
# Входные данные
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# 9
# Правильный ответ
# OK
# Access denied
# Access denied
# OK
# OK

n = int(input("Введите число файлов n "))
strings = []
file_dict = {}
for i in range(n):
    strings.append(str(input("Введите название файла и операции с ним через пробел ")))
    str_to_dict = strings[i].split()
    if len(str_to_dict) == 1:
        file_dict[str_to_dict[0]] = 0
    if len(str_to_dict) == 2:
        file_dict[str_to_dict[0]] = str_to_dict[1]
    if len(str_to_dict) == 3:
        file_dict[str_to_dict[0]] = str_to_dict[1], str_to_dict[2]
    if len(str_to_dict) == 4:
        file_dict[str_to_dict[0]] = str_to_dict[1], str_to_dict[2], str_to_dict[3]

m = int(input("Введите кол-во запросов к файлам m "))
operations = []
oper_dict = {}
for i in range(m):
    operations.append(str(input("Введите операцию с маленькой и название файла для применения операции через пробел ")))
    oper_to_dict = operations[i].split()
    if oper_to_dict[0] == "read":
        oper_to_dict[0] = "R"
    if oper_to_dict[0] == "write":
        oper_to_dict[0] = "W"
    if oper_to_dict[0] == "execute":
        oper_to_dict[0] = "X"
    oper_dict[oper_to_dict[1]] = oper_to_dict[0]

for key in oper_dict:
    if oper_dict[key] == file_dict[key]:
        print("ok")
    else:
        print("access denied")


