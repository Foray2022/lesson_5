# Задание
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Решение

change_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('test_4.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(change_rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('test_4_new.txt', 'w') as file_2:
    file_2.writelines(new_file)

