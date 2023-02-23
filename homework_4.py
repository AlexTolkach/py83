# Exercise 1
# numb = int(input('enter "n":'))
# counter = 0
# if numb == 0:
#     print(numb)
# while counter < numb:
#     counter += 1
#     print(counter)
#
# Exercise 2
# num = int(input('enter "n":'))
# summ = 0
# numbers = 0
# while (numbers + 1) < num:
#     summ = summ + (numbers + 2)
#     numbers += 2
# print(summ)
# if num < 0:
#     while (numbers - 1) > num:
#         summ = summ + (numbers - 2)
#         numbers -= 2
#     print(summ)
#
# Exercise 3
# nub_n = int(input('enter number:')[::1])
# summ = 1
# while nub_n != 0:
#     n = nub_n % 10
#     nub_n = nub_n // 10
#     if n % 2 == 0 and n != 0:
#         summ = summ * n
# print(summ)
#
# Exercise 4
# numb = int(input('enter "n":'))
# numbers = 0
# n = 0
# while n <= numb:
#     numbers += 1
#     n = numbers ** 2
#     if n > numb:
#         break
#     print(n, end=' ')
#
# Exercise 5
# numb = int(input('enter "n":'))
# numbers = 0
# n = 0
# while n <= numb:
#     numbers += 1
#     n = numbers ** 2
# print(n)
#
# Exercise 6
# numb_n = abs(int(input('enter "n":')))
# numb_n = str(numb_n)[::-1]
# while True:
#     n = int(numb_n) % 10
#     print(n)
#     break
#
# Exercise 7
# num_n = int(input('enter "n":'))
# summ = 0
# while num_n != 0:
#     n = num_n % 10
#     num_n = num_n // 10
#     summ = summ + n
# print(summ)
#
# Exercise 8
# 8.	Дано натуральное число n. Найти значение минимальной цифры в данном числе .
# num_n = int(input('enter "n":'))
# minimal = 10
# while num_n != 0:
#     n = num_n % 10
#     num_n = num_n // 10
#     if minimal > n:
#         minimal = n
# print(minimal)

# Задачи на строки
# Exercise 1
# string = input('enter string:')
# letter_z = 'z'
# temp = ''
# for ind in range(len(string)):
#     temp += string[ind]
#     if string[ind] == letter_z:
#         temp += '!'
# print(temp)
#
# Exercise 2
# string = input('enter string:')
# temp = ''
# for ind in range(len(string)):
#     if string[ind] not in temp:
#         temp += string[ind]
# print(temp)
#
# Exercise 3
# string = input('enter string:' + ' ')
# temp = ''
# for i in range(len(string)):
#     if string[i] == and string[i + 1].isdigit():
#         continue
#     temp += string[i]
# print(temp)
#
# string = input('enter string:')
# temp_1 = ''
# letters ='abcdefghijklmnopqrstuvwxz'
# for symbol in range(len(string)):
#     if string[symbol] not in letters:
#         temp_1 += string[symbol]
# print(temp_1)

# Exercise 4
# 4.	Дан текст. Слова в тексте разделены одним или несколькими пробелами.
# Написать программу определяющую количество слов, заканчивающихся одной и той же буквой ‘k’
# 1 подход (списки)
# string = input('enter string:')
# lst = string.split()
# print(lst)
# count = 0
# for elem in lst:
#     if elem[-1] == 'k':
#         count += 1
# print(count)
#
# print(len([elem for elem in lst if elem[-1] == 'k']))
# print(len([elem for elem in string.split() if elem[-1] == 'k']))

# 2 не зная списков
# string = input('enter string:' + " ")
# temp = ''
# count = 0
# for ind in range(len(string)):
#     if string[ind] != " ":
#         temp += string[ind]
#     elif temp:
#         if temp[-1] == 'k':
#             count += 1
#         print(temp)
#         temp = ''
# print(count)

# 3 генератор в одну строку
# s = input('enter string:' + " ")
# print([s[ind] for ind in range(len(s)) if s[ind] == 'k' and s[ind + 1] == ' '])

# Exercise 5
# string = input('enter string:').lower() + ' '
# temp = ''
# for ind in range(len(string)):
#     if string[ind] != string[ind + 1]:
#         temp = temp + str(string.count(string[ind])) + string[ind]
#         ind += 1
#         if ind == len(string) - 1:
#             break
# print(temp)


# коровы
# n = int(input())
# for i in range(1, n + 1):
#     if i % 10 == 1 and i % 100 != 11:
#         print(f"{i} корова")
#     elif (i % 10 == 2 or i % 100 != 12) or (i % 10 == 3 and i % 100 != 13) or (i % 10 == 4 and i % 100 != 14):
#         print(f"{i} коровы")
#     else:
#         print(f"{i} коров")
