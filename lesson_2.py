# Alt + Ctrl + L - автоматическая перестройка кода под PEP8

# Логические выражения (boolean)
# >(больше) >= (больше или равно) < (меньше или равно)
# != (не равно) == (равно) - проверяется по значению is (есть) - проверяется по ячейке памяти
# and (и) or (или) not(не) Xsor(одно или)
# краткие операции -= *= /= //=

# print(5 == 6)  # False
#
# var1 = 0
# var2 = 0
# print(var1 is var2)
# print(id(var1), id(var2))
# # для упрощения числа с разными значениями записываются в одну ячейку памяти
#
# var1 = 'hello world'
# var2 = 'hello world'
# print(var1 is var2)
# print(id(var1), id(var2))
#
# print(5 == 5 and 6 > 3)
# print(5 == 5 or 6 > 3)
# print(not (5 == 5) or 6 > 3)
# print(not (5 == 5) or 6 > 3)
#
# Проверка на четное число
# print(14 % 2 == 0)

# операторы пишутся внутри логического выражения (if)
# number = int(input('enter number:'))
# if number > 0:      # условие ? True/False
#     # Тело условного оператора
#     print('positive')
#     print(number + 2)
#     if number >= 10 and number < 100:
#         print('двузначное число')
# elif number == 0:
#     print('zero')
# else:                      # Два else писать нельзя
#     print('negative')
#     print(number - 2)
#
# print('end program')


# season = input('enter season of year:')
#
# if season == 'winther':
#     print('winter is here')
# elif season == 'autum':
#     print('autum is here')
# elif season == 'spring':
#     print('spring is here')
# elif season == 'summer':
#     print('summer is here')
# else:
#     print('unknown season')

# если кол-во пробелов не равно 4 функция все равно будет работать
# пробел это тоже символ

# a, b, c = map(int, input('enter lines of triangle:').split())
# if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0
#     if a == b == c:
#         print('равносторонний')
#     elif a == b or a == c or b == c:
#         print('треугольник равнобедренный')
#     else:
#        print('треугольник разносторонний')

# тернарный оператор (if записанный в одну строчку)
# что написать if условие верно else что написать
# number = int(input())
# print('четное' if number % 2 == 0 else 'нечётное')

# Строки str '' "" многострочный комментарий тоже строка
# \n перенос курсора \t табуляция \a перенос курсора в начало строки


# Учить методы строк

# some_str = """
# hello world
# I learn python
# """
# some_str = some_str.replace('\n', ' ')
# print(some_str)
# print(repr(some_str))

# str_1 = 'hello'
# str_2 = 'world'
# print(str_1 + str_2)

# в Python есть обратная индексация -1 -2 -3

# name = 'JoHn'
# print(name[2])
# print(name.islower())                 # приставка is проверяет все ли в строке буквы в нижнем регистре
# строка в питоне не изменяемый объект

# age = "213as12  "
# if age.isdigit():
#     age = int(age)
#     print(age)
# else:
#   print()

# name = 'Jhon Watson'
# slise (срез) str[start:end:step] str[start:end] str[::end]
# print(name[0:4:1])
# print(name[5:])
# print(name[1:4])
# print(name[-8:-11:-1])
# print(name[3:0:-1])
# print(name[::2])
# print(name[::-1])  # вывод в обратном порядке
# print(name[:2] + name[5:8])

# name1 = "Jhon"
# name2 = "Pit"
# print(name1 == name2)
# print(name1 < name2)  # Если первый символ одинаковый сравнивает по следующему

# name = "Jhon Watson"
# str1 = name[:4]
# str2 = name[5:]
# name2 = str2 + " " + str1
# print(name2)

# str1 = "192.168.0.1"
# print(str1.replace('.', ' '))
# print(int(str1[0:3]) + int(str1[4:7]) + int(str1[8]) + int(str1[10]))
#
# var = 1
# if var:
#     print(var)  # True (все что не 0 == True)
#
# var = 1
# if not var:
#     print(var)
#
# var1 = 10
# var2 = 2
# exp = var1 > var2
# if exp:
#     print(var)

# тернарный оператор (if записанный в одну строчку)
# что написать if условие верно else что написать
# number = int(input())
# print('четное' if number % 2 == 0 else 'нечётное')

# Строки str '' "" многострочный комментарий тоже строка
# \n перенос курсора \t табуляция \a перенос курсора в начало строки

# some_str = """
# hello world
# I learn python
# """
# some_str = some_str.replace('\n', ' ')
# print(some_str)
# print(repr(some_str))
