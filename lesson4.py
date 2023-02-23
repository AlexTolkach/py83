# for number in range(1, 12, 2):
#     print(number)
#     if number % 2 == 1:   # вывод нечетных
#        print(number)
#
# for number in range(12, -8, -1):
#     if number % 2 == 1:   # вывод нечетных
#         print(number)

# s = 'hello world'
# for sum in s:
#     print(sum)
# for ind in range(0, len(s), 1):
#     print(ind, s[ind])
#
# s = 'hello world'
# for summ in s:
#     print(sum)
# for ind in range(0, len(s), 1):
#     print(ind, s[ind])


# цикл с условием while(пока)
# cout_dish = 0
# answer = input('введите есть ли посуда(да/нет):')
# while answer == 'да':     # true/false
#     print('берем тарелку, моем, сушим')
#     answer = input('введите есть ли посуда(да/нет):')
#     cout_dish += 1
# print('мы вымыли', cout_dish, 'посуды')
# if cout_dish != 0:
#     print('идем отдыхать')
# else:
#     print('ктото помыл посуду за насд')

# cout_dish = 0
# while True:     # бесконечный цикл
#
#     answer = input('введите есть ли посуда(да/нет):')
#     if answer == 'нет':
#         break      # цикл досрочно прерывается
#     print('берем тарелку, моем, сушим')
#     cout_dish += 1
#
# print('мы вымыли', cout_dish, 'посуды')
# if cout_dish != 0:
#     print('идем отдыхать')
# else:
#     print('кто то помыл посуду за насд')

# вывести все числа от 1 до n с помощью whail:
# n = int(input('введите конечное число:'))
# begin = 1
# while begin <= n:
#     print(begin, end=' ')
#     begin += 1
# print('цикл завершён')
#
# for i in range(1, n + 1):
#     print(i, end=' ')

# статистика рождаемости
# stat = int(input('введите кол-во новорожденных в день:'))
# count_babies = 0
# while stat > 0:
#     count_babies += stat
#     stat = int(input('введите кол-во новорожденных в день:'))
# print('кол-во новорожденных:', count_babies)


# count_babies = 0
# count_days = 0
# while True:
#     stat = int(input('введите кол-во новорожденных в день:'))
#     if stat == 0:
#         break
#     count_babies += stat
#     count_days += 1
# print('кол-во новорожденных:', count_babies)
# print('кол-во дней:', count_days)

# count_babies = 0
# count_days = 0
# while True:
#     stat = int(input('введите кол-во новорожденных в день:'))
#     if stat == 0:
#         break
#     if stat > 10:
#         continue   # пропускает действия после него
#     count_babies += stat
#     count_days += 1
# print('кол-во новорожденных:', count_babies)
# print('кол-во дней:', count_days)

# дано число - вывести все его цифры
# numb = int(input('введите число:'))
# numb = str(numb)[::-1]
# numb = int(numb)
# while numb != 0:
#     n = numb % 10
#     print(n)
#     numb = numb // 10

# numb = int(input('введите число:')[::-1])
# while numb != 0:
#     n = numb % 10
#     print(n)
#     numb = numb // 10

# дано число - вывести все его цифры
# numb = (input('введите число:'))
# for n in numb:
#     print(n)

# сложить все числа числа
# sum = 0
# numb = (input('введите число:'))
# for n in numb:
#     sum += int(n)
# print(sum)

# найти НОД двух чисел
# numb, numb2 = map(int,input().split())
# numbers = min(numb, numb2)
# nod = 1
# while True:
#     if numb % numbers == 0 and numb2 % numbers == 0:
#        nod = numbers
#     numbers += 1
#     if numbers > numb or numbers > numb2:
#         print('nod is', nod)
#         break

# строки
# строка итерируемый объект
# строка не изменяемый объект

# s = 'hello'
# print(id(s))
# s = s.upper()
# print(id(s))
# s = s.lower()
# print(id(s))

#   012345678910
# len(s) = 11
# s = 'hello world'
# temp = ''
# for ind in range(len(s)):
#     if ind == len(s) - 2:
#         temp += s[ind].upper()
#         continue
#     temp += s[ind]
#     print(ind)
# print(temp)

# in в
# not in не в

# print('o' in 'hello')
# print('o' not in 'hello')

# s = 'hello world'
# gl = 'aeyuioAEYUIO'
# temp = ''
# print(len(s))
# for ind in range(len(s)):
#     print(s[ind])
#     if s[ind] not in gl:
#         temp += s[ind]
# print(temp)

#
# text = 'dog    cat       frog    mouse   '
# temp = ''
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp:     # если строка существует (она не пустая)
#         print(temp)
#         temp = ''

# text = 'dog    cat       frog    mouse   '
# temp = ''
# letter = 'o'
# count = 0
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp:     # если строка существует (она не пустая)
#         if letter in temp:
#             print(temp)
#             count +=1
#         temp = ''
# print(count)

# name = 'Jhon'
# age = 45
# print('name:', name, 'age', age)
# f-string f-нотации
# s = f'name: {name} age: {age}'
# print(s)
# print(f'name: {name} age: {age}')
# приорететно для использования
# print(f'name: {name.upper()} age: {age - 3}')

# ипользовалось в старых версиях питона
# выыод строки через спецификаторы
# %s - string
# %f - float
# %d - int
# print(f'name: %s age: %d' % (name, age))

# numb 1.. 11
# number = int(input('enter number:'))
# count = 0
# for numb in range(1, number + 1):
#     if number % numb == 0:
#         count += 1
#         print(numb)
# if count == 2:
#     print('простое')
# else:
#     print('не простое')


# mult = 1
# for i in range(5, 21):
#     mult *= i
# print(mult)
# n = int(input('enter korow'))
# for cow in range(1, n + 1):
#     if cow % 10 == 1 and cow % 100 != 11:
#         print(f"{cow} корова")

# взаимно простые числа - числа  с нод = 1 (4, 5) (12, 29) (15, 16)
# n, m = map(int, input("enter n, m").split())
# for numb in range(2, m + 1):
#     temp_numb = numb
#     temp_n = n
#     while temp_numb != 0 and temp_n != 0:
#         if temp_numb > temp_n:
#             temp_numb > temp_n
#         else:
#             temp_n %= temp_numb
#
#     if temp_n + temp_numb == 1:
#         print(f"{numb} is simpl with {n}")
