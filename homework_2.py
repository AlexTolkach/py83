# # Задачи на условный оператор
# # Exercise 1
# number = int(input("enter number:"))
# print(number % 10 == 3)
#
# # Exercise 2
# number_a, number_b, number_c = map(int, input("enter three numbers separated by a space:").split())
# print(number_a < 0 or number_b < 0 or number_c < 0)
#
# # Exercise 3
# number_n, number_k = map(int, input("enter three numbers separated by a space:").split())
# print(number_n % 2 == 0 and number_k % 2 == 0)
# print(number_n % 2 == number_k % 2)
#
# # Exercise 4
# number = int(input("enter number:"))
# print(number % 3 == 0 and number % 10 == 5)
#
# # Exercise 5
# number_a, number_b, number_c = map(int, input("enter three numbers separated by a space:").split())
# counter = 0
# if number_a % 2 == 0:
#     counter = counter + 1
# if number_b % 2 == 0:
#     counter = counter + 1
# if number_c % 2 == 0:
#     counter = counter + 1
# print(counter)
#
# if number_a % 2 == 0 and number_b % 2 == 0 and number_c % 2 == 0:
#     print("Введено три чётных числа")
# elif number_a % 2 == 0 and number_b % 2 == 0 or\
#      number_b % 2 == 0 and number_c % 2 == 0 or\
#      number_c % 2 == 0 and number_a % 2 == 0:
#     print("введено два чётных числа")
# else:
#     print("все числа не чётные")
#
#
# # Exercise 6
# number = int(input("enter a two-digit number:"))
# if number // 10 + number % 10 >= 10:
#     print("Да")
# else:
#     print("Нет")
#
# # Exercise 7
# number = int(input("enter a four-digit number:"))
# print(number % 1111 == 0)
# if number // 1000 == number % 1000 // 100 == number % 100 // 10 == number % 10:
#     print("Все цифры одинаковы")
# else:
#     print("Цифры не одинаковы")
#
# Exercise 8
# year = int(input("enter year:"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный")
# else:
#     print("Не високосный")

# # Задачи на строки
# # Exercise 1
# string1 = input("enter string 1:")
# print(string1[2])
#
# string2 = input("enter string 2:")
# print(string2[-2])
#
# string3 = input("enter string 3:")
# print(string3[:5])
#
# string4 = input("enter string 4:")
# print(string4[:-2])
#
# string6 = input("enter string 6:")
# print(string6[1::2])
#
# string7 = input("enter string 7:")
# print(string7[::-1])
#
# string8 = input("enter string 8:")
# print(string8[-1::-2])
#
# string9 = input("enter string 9:")
# print(len(string9))
#
# # Exercise 2
# word = input("enter word:")
# if word[0] == word[-1]:
#     print("Верно")
# else:
#     print("Не верно")
#
# # Exercise 3
# word = input("enter word:")
# print(word[1:4])
#
# # Execise 4
#
# apple = "яблоко"
# print(apple[1:-1], apple[3:])
#
# # Exercise 5
# print("*" * 5)
#
# # Exercise 6
# string = input("enter word:")
# if string == string[::-1]:
#     print("строка является палиндромом.")
# else:
#     print("строка не является палиндромом")
#
# # Exercise 7
#
# string = input("enter string:")
# if string.count("f") == 1:
#     print("Индекс буквы "f":", + string.find("f"))
# elif string.count("f") > 1:
#     print("Индекс первого вхождения буквы "f":", + string.find("f"), "Кол-во вхождений буквы "f":", + string.count("f"))
#
# # Exercise 8
# string = input("enter string:")
# if string.count("f") > 1:
#     print(string.find("f", string.find("f") + 1))
# elif string.count("f") == 1:
#     print(-1)
# else:
#     print(-2)
#
# # Exercise 9
# string = input("enter string:")
# print(string.replace("1", "one"))
#
# # Exercise 10
# string = input("enter string:")
# string = string.lower()
# number_symbol = len(string)
# number_g = string.count("g")
# number_c = string.count("c")
# print(int((number_g + number_c) / number_symbol * 100))

# # найти наибольшее число
# numb1, numb2, numb3 = map(int, input('введите три числа:').split())
# max_el = numb1
# if max_el < numb2:
#     max_el = numb2
# if max_el < numb3:
#     max_el = numb3
# print(max_el)
