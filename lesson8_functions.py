# global scope -глобальная область
# unmutable(неизменяемая) в функцию передаются по значению
# mutable(изменяемые) передаются в функцию по ссылке
# процедура (функция которая ничего не возвращает)
# *args - позиционные аргументы
# balance=5000
# **kwards key word arguments

# people = ['Karl', 'Vasya', 'Petya']
# def workers():
#     people.append('Anna')
#     print(people)
#
# workers()

# def workers(balance, *args):
#     print(balance)
#     print(args)
#
#
# workers('Vasya', 'Petya')

# def workers(date, *args, balance, balance_many=1000, **kwargs):
#     print(date)
#     print(balance)
#     print(args)
#     print(kwargs)
#     print(balance_many)
#
#
# workers('06.08.2020', 'Vasya', 'Petya', balance=5000, balance_many=8888, balance1=6000, balance2=7000)
#
#
# def fun(*args, **kwargs):
#     pass

# анонимные функции
# fun = lambda x, y, *args, **kwargs: x + y
#
#
# def fun_2(x, y):
#     return x + y


# print(fun_2(2, 1))
# print(fun(5, 2))


# def chet(number):
#     return not number % 2
# lst = [5, 2, 3, 4, 9, 8]
# lst.sort(key=chet)
# lst.reverse()
# print(lst)


# lst = [5, 2, 3, 4, 9, 8]
# lst.sort(key=lambda numb: not numb % 2)
# lst.reverse()
# print(lst)

# kr = lambda x: 'YES' if x % 3 == 0 else 'NO'

#print(kr(7))


# kr = lambda x: True if x % 3 == 0 else False
# print(kr(8))

# lst = ['Jhon', 'Maryz', 'Willy']
# lst.sort(key= lambda x: x[-1])
# print(lst)

# lst = ['Jhon', 'Maryz', 'Willy', 'Mar']
# lst.sort(key= lambda x: len(x))
# print(lst)

# lst = ['Jhon', 'Maryz', 'Willy', 'Mar']
# lst.sort(key=len)
# print(lst)

# map

# a, b, c = map(int, input().split())
# print(a, b, c)

# lst = [5, 6, 64, 8]
# lst = list(map(lambda x: x**3, lst))
# print(lst)


# a, b, c = map(int, ['1', 2, 3.56])
# print(a, b, c)

# lst = [5, 6, 64, 8]
# lst = list(map(lambda x: x**3 if x % 2 == 0 else x ** 5, lst))
# print(lst)

# balanse = {'jhon': 231, 'Mark': 199}

# for name in map(lambda name, money: balanse[name] + 20 if balanse[name] < 200 else balanse[name], balanse):
#     print(balanse)

# filter
# lst = [2, 3, 3, 5, 9, 6, 7, 6, 4]
# lst2 = list(filter(lambda x: not x % 2, lst))
# print(lst2)

# words = ['hello', 'world', 'price', 'gold']
# words2 = list(filter(lambda w: 'o' in w, words))
# print(words2)

# words = ['hello', 'world', 'price', 'gold']
# words2 = list(filter(lambda elem: len([sym for sym in elem if sym in 'aeyuio']) == 2, words))
# print(words2)

# global
# x = 2
# def fun():
#     global x
#     x += 3
#     print(x)
#
# fun()

# def fun():
#     def wrapper():
#         print('hello')
#     wrapper()
# fun()

# def fun(numb):
#     print(numb)
#     def wrapper():
#         print('hello')
#     wrapper()
# fun(42)

# def fun(numb):
#     def wrapper():
#         nonlocal numb
#         numb += 1
#         print(numb)
#     wrapper()
# fun(42)

# global
# local
# enclosing - замыкающая область
# built-in - встроенные функции в питоне

# Замыкание
# def person(name):
#     def wrapper():
#         print(name.capitalize())
#     return wrapper
#
# p = person('Oleg')
# print(p)
# p()
# clousure

# замыкание
# def counter(x):
#     def wrapper(a):
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper
# c = counter(0)
# c(1)
# c(1)
# c(1)

# def counter_2(x):
#     return x + 1
#
#
# print(counter_2(1))
# print(counter_2(1))
# print(counter_2(1))


# !!!Декораторы - функция которая принимает функцию её же модернизирует и возвращает обратно
# def say():
#     print('Hello')
#
#
# def decorator(fun):
#     def wrapper():
#         print('before decorated')
#         fun()
#         print('after decorated')
#
#     return wrapper
#
#
# decor_say = decorator(say)
# say()

# def greeting(name: str):
#     return 'Hello ' + name
#
#
# def decorator(fun):
#     def wrapper(name: str):
#         if name.capitalize():
#             return fun(name)
#         else:
#             return 'hello ' + name.capitalize()
#
#     return wrapper
#
#
# # decor_gr = decorator(greeting)
# # print(greeting('peter'))
# print(decor_gr('peter'))


# def decorator(fun):
#     def wrapper(name: str):
#         if name.capitalize():
#             return fun(name)
#         else:
#             return 'hello ' + name.capitalize()
#
#     return wrapper
#
# @decorator
# def greeting(name: str):
#     return 'Hello ' + name
# # decor_gr = decorator(greeting)
# # print(greeting('peter'))
# print(greeting('peter'))

# users = {'Jhon': 1234, 'Jack': 590, 'Anna': 900}
#
#
# def balance(**kwargs):
#     for name, price in kwargs.items():
#         if price < 1000:
#             kwargs[name] += 100
#     return kwargs
#
#
# users = balance(**users)
# print(users)
