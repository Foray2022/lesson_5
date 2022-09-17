# Задание
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

# Решение

with open('test_5.txt', 'w+') as file:
    line = input('Enter the numbers separated by a space: \n')
    file.writelines(line)
    my_numb = line.split()

    print(sum(map(int, my_numb)))
