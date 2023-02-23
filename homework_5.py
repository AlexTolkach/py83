# Задачи на кортежи
# Exercise 1
# tup = (3, 28, 4, 6, 24, 28, 30, 40)
# numbers = ''
# count = 0
# for num in tup:
#     for i in range(1, num):
#         if num % i == 0:
#             count += i
#     if count == num:
#         print(num)
#     else:
#         count = 0

# Exercise 2
# tup = (35, 28, 4, 6, 24, 28, 30, 40)
# print(max(tup) - min(tup))

# Exercise 3
# tup = (-4, 5, 2, -2, 7, -8, -9, 1)
# counter = 0
# negative = tup[0] < 0
# for num in range(len(tup)):
#     if (tup[num] < 0) != negative:
#         counter += 1
#     negative = tup[num] < 0
# print(counter)

# Exercise 4
# tup = (2, 17, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16, 17)
# count = 0
# for num in tup:
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             count += 1
#     if count <= 0:
#         print(num)
#     else:
#         count = 0

# Exercise 5
# Дан кортеж. Найти максимальную по длине монотонную последовательность (убывающую или возрастающую) чисел.
# tup = (5, 2, 6, 8, 9, 7, 5, 7, 8)
# count = 1
# max_count = 0
# for ind in range(len(tup) - 1):
#     if tup[ind] < tup[ind + 1]:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 1
# print(max_count)

# Exercise 6
# tup = (1, 2, 4, 1, 2, 6, 6)
# ind = 0
# count = 0
# for elem in tup:
#     count += 1
# while ind != count:
#     if tup[ind] in tup[ind + 1:]:
#         print(tup[ind], end=" ")
#         ind += 1
#     else:
#         ind += 1

# Задачи на списки

# Exercise 7.
# lst = list(map(int, input('enter a list of numbers:').split()))
# print(lst)
# for num in lst:
#     if num % 2 == 0:
#         print(num)

# Exercise 8
# lst1 = list(map(int, input('enter a list1 of numbers:').split()))
# lst2 = list(map(int, input('enter a list2 of numbers:').split()))
# lst = []
# for elem1 in lst1:
#     if elem1 not in lst2:
#         lst.append(elem1)
# if not lst:
#     print("no data")
# print(min(lst))

# Exercise 9
# lst = list(map(int, input("enter a list of numbers:").split()))
# count = 0
# for elem in range(len(lst) - 1):
#     if lst[elem] > lst[elem + 1]:
#         count += 1
# print(count)

# Exercise 10
# lst = list(map(int, input("enter a list of numbers:").split()))
# # lst = [18, 42, 8, 122]
# new_lst = []
# new_num = 0
# for num in lst:
#     new_lst.append(num)
#     if num % 2 == 0:
#         while num > 0:
#             num1 = num % 10
#             num = num // 10
#             new_num = new_num * 10
#             new_num = new_num + num1
#         new_lst.append(new_num)
#         new_num = 0
# print(new_lst)

# Exercise 11
# lst = list(map(int, input("enter a list of numbers:").split()))
# for ind in range(len(lst):
#    if lst.index(lst[ind]) == ind:
#        print(f"Число {elem} встречается {lst.count(elem)} раз")

# Exercise 12
# lst = list(map(int, input("enter a list of numbers:").split()))
# count = 0
# for elem in lst:
#     if lst.count(elem) == 1:
#         lst.append(elem)
# print(lst)

