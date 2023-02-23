# все задачи вводим через input()
# факториал 5 = 1*2*3*4*5 = 120
# взаимно простые это когда НОД(наиобольший общий делитель) равен 1 (2 10 ( 3 5 7 9))
#
# Exercise 1
# 1. Вывести на экран число "10" 20 раз столбиком
# for numb in range(20):
#     print('10')
#
# Exercise 2
# 2.Даны два числа a и b. Составить программу вывода на экран всех чисел от a до b.
# numb_a, num_b = map(int, input('enter a, b:').split())
# num_b = num_b + 1
# for numb in range(numb_a, num_b):
#     print(numb)
#
# Exercise 3
# numb_n = int(input('enter n:'))
# numb_n += 1
# for num in range(1, numb_n):
#     print(num ** 3, end=' ')
#
# Exercise 4
# for num in range(100, -101, -1):
#     print(num, end=' ')
#
# Exercise 5
# a = int(input('enter a:'))
# b = a ** 10 + 1
# for num in range(a, b):
#     if num % 2 == 0:
#         print(num)
#     elif a == 1:
#         print('нельзя составить отрезок от 1 до 1')
#
# Exercise 6
# summ = 0
# for num in range(100, 501):
#     summ = summ + num
#     print(summ)
#
# Exercise 7
# product_of_numbers = 5
# for num in range(6, 21):
#     product_of_numbers = product_of_numbers * num
#     print(product_of_numbers)
#
# Exercise 8
# numb = int(input('enter "n":'))
# factorial = 1
# for numbers in range(1, numb + 1):
#     factorial = factorial * numbers
# print(factorial)
#
