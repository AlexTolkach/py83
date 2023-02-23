# # Задачи на множества
# # Exercise 1
# numbers = list(map(int, input('Enter the numbers through the gap:').split()))
# print(numbers)
# count = 0
# ind = 0
# for num in numbers:
#     count += 1
# while ind < count:
#     if ind == 0:
#         print(f"NO: {numbers[ind]}")
#         ind += 1
#     if numbers[ind] in numbers[0:ind - 1]:
#         print(f"YES: {numbers[ind]}")
#         ind += 1
#     else:
#         print(f"NO: {numbers[ind]}")
#         ind += 1
#

# set1 = set()
# for elem in lst:
#     if elem not in set1:
#         print("NO")
#         set1.add(elem)
#     else:
#         print("YES")

# # Exercise 2
# number_n = int(input('enter number n:'))
# number_avgust = 6
# set_number_avgust = {6}
# range_number_avgust = {i for i in range(1, number_n + 1)}
# numbers_beatrice = set(map(int, input('numbers named by Beatrice:').split()))
# while True:
#     if numbers_beatrice == set_number_avgust:
#         print('YES')
#         print(f'Вы выиграли, Август загадал число: {number_avgust}')
#         break
#     elif number_avgust not in numbers_beatrice:
#         print('NO')
#         range_number_avgust.difference_update(numbers_beatrice)
#         print(range_number_avgust)
#         numbers_beatrice = set(map(int, input('numbers named by Beatrice:').split()))
#         if len(range_number_avgust) < 3:
#             print(f'Вы проиграли, Август загадал число {number_avgust}')
#             break
#     elif number_avgust in numbers_beatrice:
#         print('YES')
#         range_number_avgust.intersection_update(numbers_beatrice)
#         print(range_number_avgust)
#         numbers_beatrice = set(map(int, input('numbers named by Beatrice:').split()))
#
# # Задачи на словари
# # Exercise 3
# school = {}
# school["9а"] = 30
# school.update({'9б': 25, '9в': 22, '9г': 31, '9д': 21})
# school['9а'] = 18
# school.update({"9ю": 40})
# school.pop('9ю')
# total = sum(school.values())
# print(total)
# print(school)
#
# # Exercise 4
# definition = input("Введите определение и значение через тире:")
# key_2 = []
# key = []
# value = []
# dic = {}
# ind = 0
# numb = ''
# while definition != '.':
#     if '–' not in definition:
#         print('Вы не разделили определение и значение знаком тире')
#         definition = input("Введите определение и значение через тире:")
#
#     else:
#         k, v = definition.split('–')
#         key.append(k.rstrip())
#         value.append(v.lstrip())
#         dic = dict(zip(key, value))
#         definition = input("Введите определение и значение через тире:")
#
# while type(numb) != int:
#     numb = input('Введите целое число:')
#     if numb.isdigit():
#         numb = int(numb)
#     else:
#         print('Вы не ввели целое число')
#
#
# count = 0
# while count != numb:
#     key_2.append(input('Введите значение:'))
#     count += 1
#
# for elem in key_2:
#     if dic.setdefault(elem) is None:
#         print('Не найдено')
#         ind += 1
#     else:
#         print(dic.setdefault(elem))
#         ind += 1

# Exercise 5
# Решили на занятии

# Дополнительные задачи на использование всех коллекций
# Exercise 1
# lst = list(map(int, input("enter numbers:").split()))
# lst2 = list()
# for elem in lst:
#     lst2.append(elem)
#     lst2.append(0)
# print(lst2)

# Exercise 2
# numb = int(input('enter n:'))
# subsequence = list()
# for ind in range(1, numb + 1):
#     for i in range(ind):
#         if i <= ind:
#             subsequence.append(str(ind))
#             i += 1
#     ind += 1
# print(' '.join(subsequence[:numb]))

# Exercise 3
# m = 5
# n = 5
# a = [[j ** i for j in range(m)] for i in range(n)]
# summa = 0
# ind = 0
# print(len(a))
# while ind < len(a[0]):
#     summa += a[ind][ind]
#     ind += 1

# Exercise 4
# lst = list(map(int, input('enter numbers:').split()))
# num = ''
# for ind in range(len(lst)):
#     if lst[ind] in lst[ind + 1::]:
#         if str(lst[ind]) not in num:
#             num += str(lst[ind]) + ' '
# print(num)

# Exercise 5
# string = 4
# columns = 5
# lst = [[x ** j for x in range(1, columns + 1)] for j in range(1, string + 1)]
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j], end=' ')
#     print()

# Exercise 6
# n = int(input('enter number n:'))
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input('enter numbers:').split())))
# count = 0
# for elem in lst:
#     if elem == elem[::-1]:
#         count += 1
# if count > 0:
#     print('YES')
# else:
#     print('NO')

# Exercise 7
# Не смог решить

# Exercise 8 (точная копия 4 задачи)
# lst = list(map(int, input('enter numbers:').split()))
# num = ''
# for ind in range(len(lst)):
#     if lst[ind] in lst[ind + 1::]:
#         if str(lst[ind]) not in num:
#             num += str(lst[ind]) + ' '
# print(num)

