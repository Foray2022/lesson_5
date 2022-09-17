# Задание
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк,количества слов в каждой строке.

# Решение
my_file = open('test.txt', 'r')
content = my_file.read()
print(f': \n {content}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(f'Number of lines in the file: {len(content)}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'in the line{i + 1} - Number of words {len(content[i])} {content[i].split()}')
my_file.close()
