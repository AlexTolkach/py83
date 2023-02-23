# Типы данных
# # - Однострочный коментарий

"""
многострочный комментарий

"""

# Базовые типы данных
# 1 string str строки 'hello' "wold"
# 2 integer int числа -5 6 7
# 3 float вещественные числа (с плавающей точкой 3.14)
# 4 boolean bool  True 1  /False 0

print('hello world')
print(8, 9)

number = 5     # операция присваивания
print(number)
print(type(number))    # type - просмотр типа данных


age = 25
name = 'Max'
print('name:', name, 'age:', age)

# Динамическая типизация
a = 10
print(a)
print(id(a))
a = 'hello'
print(a)
print(id(a))

# название переменных
# не называем ключевыми словами print type if for else
# не начинаем с цифры
# нельзя использовать бинарные символы @ +-%*,
# нельзя использовать русские буквы

# базовые арифметические операции
# + - * **(возведение в степень); / (обычное деление); //(целочисленное деление); %(деление без остатка)

number_1 = 10
number_2 = 3
result = number_1 % number_2
print(result)


# базовые операции со строками
some_string = 'hello'
print(some_string + " ")   # конкотенация строк
print(some_string * 5)   # умножение строк
print(some_string + str(5))   # смена типа данных


some_string = "2145"
numb = 0
logik = bool(some_string)
print(logik)


# number = (input("enter age:"))  # ввод данных, input - это тип данных строка
# print(numb)

# x = int(input("enter x:"))
# y = int(input("enter y:"))
# res = (x + y) ** 23 - 5 + (5 / 7)
# print(res)

# length_cube = float(input('enter length:'))
# print(length_cube ** 2)
# print(length_cube ** 2 * 6)
# print(length_cube ** 3)

number = 451
x = number // 100
y = number % 100 // 10
c = number % 10
print(x, y, c)

number_2 = c * 100 + y * 10 + x
print(number_2)

print(20 // 30)

# var1, var2, var3 = map(int, input("enter variables:").split())
# print(var1)
# print(var3)
# print(var2)

# перемена местами переменных

tor1 = 5
tor2 = 4
print(tor1, tor2)
tor1, tor2, = tor2, tor1
print(tor1, tor2)

