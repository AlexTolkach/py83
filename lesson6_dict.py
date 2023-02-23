# словари dict(key : value) ассоциативный массив
# key unique - ключи уникальны, unmutable(неизменяемы)
# key - str int float bool tuple
# value - любой, могут повторяться

# перебор элементов
# friend_phone = {"Vasya": 231752564, "Anna": 23458559916}
# for friend in friend_phone:
#     print(friend, friend_phone[friend])
#
# for friend, phone in friend_phone.items():
#     print(friend, phone)
#
# for phone in friend_phone.values():
#     print(phone)
#
# for phone in friend_phone.keys():
#     print(phone)

# friend_phone["Angelina"] = 66564916344
# print(friend_phone)

# если добавить сстарый ключь с новым значением то значение заменится в старом ключе

# добавляет пары ключ - значение
# friend_phone.update({"Paul": 6564687946})

# проверка на вхождение ключа
# if "Vasya" not in friend_phone:
#     friend_phone.update({"Paul": int(input())})
# print(friend_phone)

# удаление по ключу
# friend_phone.pop("Vasya")

# friend_phone.fromkeys([1, 2, 3], 42)   ????????
# print(friend_phone)

# вывод значения по ключу
# print(friend_phone["Vasya"])
