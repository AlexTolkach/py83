# Exercise 1
# number = int(input('enter "n":'))
#
#
# def fib(n: int):
#     fib1 = 1
#     fib2 = 1
#     i = 0
#     while i < n - 2:
#         fib_sum = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1
#     print(fib2)
#
#
# fib(number)
#
#
# def factorial(n: int):
#     factor = 1
#     for num in range(1, n + 1):
#         factor *= num
#         num += 1
#     print(factor)
#
#
# factorial(number)

# Exercise 2
# numb = int(input('enter "x":'))
#
#
# def closet_mod_5(x: int):
#     return x if x % 5 == 0 else x + (5 - x % 5)

    # while True:
    #     if x % 5 == 0:
    #         print(x)
    #         break
    #     if x % 5 != 0:
    #         x += 1


# closet_mod_5(numb)

# Exercise 3
# var = input('enter variable name:')
#
#
# def check_variable(v):
#     while v != "Поработали, и хватит.":
#         if v[1::].isdigit() or '_' in v or v.isalpha():
#             print('Можно использовать')
#             print(v)
#             v = input('enter variable name:')
#         elif v[0].isdigit():
#             print('Нельзя использовать')
#             print(v)
#             v = input('enter variable name:')
#
#         else:
#             print('Нельзя использовать')
#             print(v)
#             v = input('enter variable name:')
#
#
# check_variable(var)

# Exercise 4
# def bank(a: int, years: int):
#     for year in range(1, years + 1):
#         a *= 1.1
#     print(f'{a} рублей будет на счету через {years} лет')
#
#
# bank(int(input("enter amount:")), int(input('How many years do you contribute:')))

# Exercise 5
# import time
#
#
# def prime_number(n: int):
#     count = 0
#     for num in range(2, n + 1):
#         for i in range(2, num // 2 + 1):
#             if num % i == 0:
#                 count += 1
#         if count <= 0:
#             print(num)
#         else:
#             count = 0
#
#
# prime_number(100)
#
#
# def decorator(fun):
#     def time_():
#         start = time.time()
#         fun(100)
#         end = time.time() - start
#         print(end)
#     return time_
#
#
# decor_num = decorator(prime_number)
# decor_num()

# Exercise 6
# import time
#
#
# def registration():
#     name = input('enter name:')
#     age = int(input('enter age:'))
#     floor = input('enter floor:')
#
#
# def decorator(fun):
#     def time_():
#         start = time.time()
#         fun()
#         end = time.time() - start
#         print(end)
#     return time_
#
#
# decor_registration = decorator(registration)
# decor_registration()
