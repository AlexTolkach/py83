# Циклы (повторение чего либа)
# цикл с параметром (цикл перебора объектов) for
# цикл с условием
# numb = 5 # numb(объект) =(оператор присваивания) 5
# for(для) var(переменая) in(в) (итерируемый объект)
# range(start, stop, step) не позваляет работать с float
# range(1, 5, 1)   1 2 3 4
# range(1, 5) 1 2 3 4    # если шаг равен 1 его можно не писать
# range(5) 0 1 2 3 4
# for elem in range(1, 10, 1):    # renge выводит диопазон
#     print(elem, end=" ")
#
# s = 'hello world'   # перебор по элементам
# for symb in s:
#     print(symb, end=" ")
#
#
# # перебор строки по индексам
# lenght = len(s)
# for i in range(len(s)):
#     print(i)
#
# animals = ['fox', 'dog', '']
# for i in animals:

#
# перебрать числа от 1 - 100 и вывести кратно 5
# for numb in range(1, 101):
#     if numb % 5 == 0:
#         print(numb ** 2, end=' ') # возвели в степень 2

# найти сумму на промежутке от 10 до 50
# summ = 0
# for numb in range(10, 51):
#     summ += numb
# print(summ)

# дано число, вывести все его делители
# делитель это число которое делит число нацело
# numbers = int(input())
# for numb in range(1 , numbers + 1):
#     if numbers % numb == 0:
#         print(numb, end=' ')
