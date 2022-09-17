# Задание
# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.

# Решение

file = open("test_6.txt", 'r', encoding='utf-8')
string = file.read().split("\n")[:-1]
print(string)

dictionary = {}

for item in string:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dictionary[key] = value
print(dictionary)

print("\n Total number of classes by subject")
for i in dictionary:
    list = dictionary[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)
file.close()
