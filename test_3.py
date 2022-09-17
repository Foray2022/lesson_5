# Задание
# Создать текстовый файл (не программно), построчно записать
# фамилии сотрудников и величину их окладов(не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Решение
with open('test_3.txt', 'r') as f:
    workers = {}
    salary = []
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: the salary is less 20000')
        salary.append(value)
print(f'average salary {sum(map(float, salary)) / len(salary)}')
