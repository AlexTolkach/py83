# Функции
# Аладин = global mainspace(глобальная область)
# Лампа и джин = функция
# исполнял 3 желания = реализация функции
# Аладин -> лампа ->Джин -> исполнял 3 желания -> возвращался в лампу
# global spsce

# lst = [4, 5, 6, 7]
#
#
# def show_list():
#     for elem in lst:
#         print(elem)
#
#
# show_list()

# def pancakes():
#     print('a')
#     print('s')
#     print('d')
#     print('f')
#     print('g')
#     for i in range(5):
#         fried()
#         print(f" порция {i + 1} готова")
#
# def fried():
#     print('a2')
#     print('s2')
#     print('d2')
#     print('f2')
#     print('g2')
#
#
# pancakes()

#                    анотация
def registr(name: str, age: int):
    print(f'Приветствую {name} {age}')


registr('Oleg', 25)
registr(age=28, name="oleg")
