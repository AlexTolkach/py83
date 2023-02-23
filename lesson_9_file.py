# files
# Режимы доступа:
# W - write - запись(все что было то пропало..)
# R - read - чтение(считываем всё из файла)
# A - append - дозапись(записывает в конец файла)
# X - запишет в файл информацию если файла не существовало
# w+ r+ a+ wb rb ab xb wb+ rb+
# import csv
# Что такое контекстный менеджер -
# enter(вход) exit(выход)

# file = open('test_file.txt', 'r', encoding='UTF_8')
# some_str = file.read()
# file.close()
# print(repr(some_str))
# lst = some_str.replace('\n', ' ').rstrip().split()
# lst = list(map(int, lst))
# print(lst)

# file = open('test_file.txt', 'r', encoding='UTF_8')
# some_str = file.read(2)
# file.close()
# print(repr(some_str))
# lst = some_str.replace('\n', ' ').rstrip().split()
# lst = list(map(int, lst))
# print(lst)

# file = open('test_file.txt', 'r', encoding='UTF_8')
# for line in file:
#     print(line.rstrip())
# file.close()

# file = open('test_file.txt', 'r', encoding='UTF_8')
# lst = []
# for line in file:
#     lst.append(int(line.rstrip()))
# file.close()
# print(lst)

# file = open('test_file.txt', 'r', encoding='UTF_8')
# students = {}
# for line in file:
#     lst = line.rstrip().split()
#     marks = list(map(int, lst[1:]))
#     students[lst[0]] = marks
#
# file.close()
# print(students)
# file_avg = open('avg_mark', 'w', encoding='UTF-8')
# for name, marks in students.items():
#     file_avg.write(name + ' ' + str(sum(marks) / 5) + '\n')
# file_avg.close()

# with open('test_file.txt', 'r', encoding='UTF-8') as file:
#     lst = []
#     for line in file:
#         lst.append(line.rstrip())
# max_len = 0
# numb = 1
# s = ''
# for id, line in enumerate(lst):
#     if len(line) > max_len:
#         max_len = len(line)
#         s = line
#         numb = id + 1
# print(s)
# print(max_len)
# print(numb)

# with open('test_file.txt', 'r', encoding='UTF-8') as file:
#     lst = []
#     for line in file:
#         lst.extend(line.rstrip().split())
# print(lst)
#
# max_lst = 0
# for word in lst:
#     if len(line) > max_lst:
#         max_lst = len(word)
# print(max_lst)

# csv comma separate values файл разделенный чаще всего запятой

# import random
# lst = [str(random.randint(1, 10)) for _ in range(100)]

# print(','.join(lst))

# with open('test_csv.csv', 'w') as file_csv:
#     file_csv.write(';'.join(lst))

# print(lst)

# lst_read = []
# with open('test_csv.csv', 'r') as file_csv_read:
#     s = csv.reader(file_csv_read, delimiter=';')
#     print(s)
#     for el in s:
#         print(el)
#         lst_read = list(map(int, el))
# print(lst_read)


# json (ключи значения)
import json
person = {
    'name': 'Jhon',
    'lastname': 'Watson',
    'age': 24
}

# dumps = сериализует объект(преобразует в строку)
print(repr(json.dumps([42, 56, 0, 2])))

with open('test_json.json', 'w', encoding="UTF-8") as file_json:
    json.dump(person, file_json, indent=4)

with open('test_json.json', 'r', encoding="UTF-8") as file_json_read:
    person2 = json.load(file_json_read)

print(person2)
