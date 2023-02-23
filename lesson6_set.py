#
# str list -
# Множества
# множества замороженое множество
# множества хранят уникальные элементы, не упорядоченные, хранит в себе только не изменяемые типы данных
#
# set_1 = set()    # пустое множество
#
# set_2 = {5, 6, -1, 'hell0', 4.22, 60, (1, 2, 3), True}
# print(set_2)
#
# # перебор по элементам
# for elem in set_2:
#     print(elem)
#
# # подсчет элементов
# print(len(set_2))
#
# # добавление элемента неизменяемого типа данных
# set_2.add(9)
# print(set_2)
#
# # добавление + распаковка (итерабельных объектов)
# set_2.update([4, 7, 15])
# print(set_2)
#
# # добавление слова целиком
# set_2.update('home'.split())
# print(set_2)
#
# # удаление случайного элемента и его вывод
# var = set_2.pop()
# print(var)
#
# # удаление елемента по значению
# set_2.discard(5)
# print(set_2)
#
# # если элемента нет выдаст ошибку
# set_2.remove(5)
# print(set_2)
#
# # проверит есть ли элимент в множестве и только потом удалит при наличии элемента
# set_2.remove(5)
# if 5 in set_2:
#     print(set_2)
#
# # очистка
# set_2.clear()
# print(set_2)

# проверка множеств
# set1 = {1, 2, 6, 7, 9}
# set2 = {2, 3, 6, 7, 11}
# print(set1.union(set2))

#
# set1 = {1, 2, 6, 7, 9}
# set2 = {2, 3, 6, 7, 11}
#print(set1.update(set2))

# обновляет текущее множество
#print(set1.intersection_update(set2))

#
#print(set1.difference_update(set2))

#
#rint(set1.symmetric_difference(set2))

# является ли set1 подмножеством set2
#print(set1.issubset(set2))

# является ли set2 подмножеством set1
# print(set2.issuperset(set1))

# заморороженое множество (не изменяется)
# set1 = {4, 2, 1, 5}
# f_set1 = frozenset(set1)

# вывод не пересекающихся чисел
# lst = [5, 2, 6, 7, 2, 5]
# lst2 = [3, 2, 6, 8, 2, 9]
# set1 = set(lst)
# set2 = set(lst2)
# print(set1 ^ set2)

#