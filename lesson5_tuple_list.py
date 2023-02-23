# # tuple (кортежи)
# #                -6  -5    -4   -3    -2  -1
# #         0      1    2     3   4     5         6
# tup = ('hello', 54, True, 5.23, 54, (1, 5, 2, (8, 9)))
# # print(tup[-1][2][1])
# print(tup[-2])
# print(tup[2])
# # print(tup[20])    # выдаст ошибку
# print(tup[1:4])
# # Кортеж не изменяемый объект
# # Нельзя изменить элемент кортежа
# # кортежи могут содержать в себе кортежи
# # методы кортежа .count(),  index()
#
#
# tup = ('hello', 54, True, 5.23, 54, )
# print(tup.count(54))
# # print(tup.index(54, 2, 4))    # выдаст ошибку
# # перебор элементов
# for elem in tup:
#     print(elem)
#
# for ind in range(len(tup)):
#     print(tup[ind])
#
# tup2 = (1, 4, 5)
# tup += tup2
# print(tup)
# print(id(tup))

# Нахождение максимального элемента
# tup = (5, 2, -2, 7, -8, -9, 1)
# max_el = tup[0]
# for i in tup:
#     if i > max_el:
#         max_el = i
# print(max_el)

# # чтоб создать кортеж для одного элемента нужно добавить ","
# tup = (5,)
# print(type(tup))
#
# # преобразование строки в кортеж
# s = 'hello'
# tup = tuple(s)
# print(tup)
#
# s = 'hello'
# tup = tuple(s.split(','))
# print(tup)

# Задачи по кортежам
# Найти максимальный элемент
# tup = (5, 6, 1, 10, 18, 5, 2)
# max_el = tup[0]
# for elem in tup:
#     if elem > max_el:
#         max_el = elem
#     print(max_el)
# print(max_el)

# List (списки)     mutable (изменяемые)
#      0   1       2      3        4          5
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# tup = (5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9])
# print(lst.__sizeof__())
# print(tup.__sizeof__())

# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst[0] = 1
# print(lst)

# добавление элементов
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# print(id(lst))
# lst += [5, 2, 6]
# print(lst)
# print(id(lst))

# при добавлении элементы распоковываются
# добавлегние в конец списка
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst.append([1, 2,3])

# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst.insert(10, 5)  #10 это инлекс, 5 элемент
# print(lst)

# удаленbt первого эллемента
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst.remove(5)
# print(lst)

# удалить все элементы
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# while 5 in lst:
#     lst.remove(5)
#     print(lst)

# удаление по индексу
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# if 5 in lst:
#     lst.remove(5)
# print(lst)

# удалить срез элементов
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# del lst[3:5]
# print(lst)

# взять часть списка
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# print(lst[1:5])

# делает список пустым
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst.clear()

# первое вхождение
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# print(lst.index(5, 0, 7))

# добавление в конец списка
# lst.extend([5, 2, 6])
# print(lst)

# сделать копию списка (создает новое хранилище, чтоб не изменить исходный список при манипуляциях)
# lst = [5, 2.42, 'hello', True, (6, 1, 2), [5, 2, 9]]
# lst2 = lst.copy()
# print(lst2)
# или полный поверхностный срез
# lst2 = lst[:]

#
# s = 'hello'
# lst = list(s)
# print(lst)

# ввести данные в список самостоятельно
# lst = []
# n = int(input("enter count of elem:"))
# for i in range(n):
#     elem = int(input('enter elem:'))
#     lst.append(elem)
# print(lst)

# list comprehension
# 1 [что хотим добавить for из чего хотим добавить in итерабильгый объект]
# lst = [numb for numb in range(1, 11)]
# print([numb for numb in range(1, 11)])
# print(lst)
# print(list('hello'))
# print([numb.upper() for numb in 'hello'])
# print([numb ** 3 for numb in range(1, 11)])

# 2 [что хотим добавить for из чего хотим добавить in итерабильгый объект if условие верно]
# print([numb ** 3 for numb in range(1, 11) if numb % 2 == 0])
# print([symb for symb in 'hello' if symb in 'AEYUIOaeyuio'])


# print("чётное" if 4 % 2 == 0 else "нечетное")   # тернарный оператор

# [что хотим добавить if если условие верно else что хотим добавить for из чего хотим добавить in итерабильгый объект if условие верно]
# print([num if num % 2 == 0 else num **2 for num in range(1, 11)])
# print([int(input()) for i in range(5)])

# ввод данных по разделителю без ограничений
# print([int(i) for i in input().split()])

#
# s = 'hello world i am Piter Parker'
# lst = list(s)
# print(lst)
# lst = s.split()
# print(lst)
# # удалить из строки слова начинающиеся с большой буквой
# lst = [elem for elem in lst if elem[0].isupper()]
# print(lst)
# # собираем строку обратно
# s = " ".join(lst)
# print(s)

# # сделать дома в одну строчку
# lst = [int(i) for i in input().split()]
# print(lst)
# lst2 = []
# if len(lst) == 1:
#     print(lst)
#     for i in range(len(lst)):
#         if i == 0:
#             lst2.append(lst[-1] + lst[1])
#         elif i == len(lst) - 1:
#             lst2.append(lst[-2] + lst[0])
#         else:
#             lst2.append(lst[i - 1] + lst[i + 1])
# print(lst2)
# lst = [1, 2, 3, 3, 4, 6, 6, 10]
# lst2 = []
# # for elem in lst:
# #     print(lst.index(elem), elem)
# # for ind, elem in enumerate(lst):
# #    print(ind, elem)
# for ind in range(len(lst)):
#     if lst[ind] not in lst2:
#         lst2.append(lst[ind])
# print(len(lst2))

# count = 0
# for i in range(len(lst)):
#     if lst[i] < lst[i + 1]:
#         count += 1
# if lst[-2] < lst[-1]:
#     count +=1
# print(count)
#
# count = 1
# ind = 0
# while ind < len(lst):
#     if ind == len(lst) - 2:
#         if lst[ind] < lst[ind + 1]:
#             count += 1
#         break
#     if lst[ind] < lst[ind + 1]:
#         count += 1
#     ind += 1
# print(count)

# найти сумму чисел пока не введем 0
# number = int(input())
# summ = 0
# count = 0
# while number != 0:
#     summ += number
#     count += 1
#     number = int(input())
#     if number > 10:
#         break
# else:                   # прикрепляется к циклу while и выводит результат если break не сработал
#     print(count)
#     print("break не исполнился")
#
# print(summ)
# print(count)
