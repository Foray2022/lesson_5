# Задание
# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Решение
my_file = open('test.txt', 'w+')
line = input('Enter the line: \n')
while line:
    my_file.writelines(line)
    line = input('Enter the line: \n')
    if not line:
        break

my_file.close()
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
