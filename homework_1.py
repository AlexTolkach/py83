# # 1 Exercise
#
# # Option 1
# print(17 / 2 * 3 + 2)
# print(2 + 17 / 2 * 3)
# print(19 % 4 + 15 / 2 * 3)
# print(15 + 6 - 10 * 4)
# print(17 / 2 % 2 * 3 ** 3)
#
# # Option 2
# expression_value_1_1 = 17 / 2 * 3 + 2
# expression_value_1_2 = 2 + 17 / 2 * 3
# expression_value_1_3 = 19 % 4 + 15 / 2 * 3
# expression_value_1_4 = 15 + 6 - 10 * 4
# expression_value_1_5 = 17 / 2 % 2 * 3 ** 3
# print(expression_value_1_1)
# print(expression_value_1_2)
# print(expression_value_1_3)
# print(expression_value_1_4)
# print(expression_value_1_5)
#
# # 2 Exercise
# # Option 1
# print((17 / 2) * (3 + 2))
# print((2 + 17) / 2 * 3)
# print(19 % (4 + 15) / 2 * 3)
# print(((15 + 6) - 10) * 4)
# print(17 / 2 % (2 * 3 ** 3))
#
# # Option 2
# expression_value_2_1 = (17 / 2) * (3 + 2)
# expression_value_2_2 = (2 + 17) / 2 * 3
# expression_value_2_3 = 19 % (4 + 15) / 2 * 3
# expression_value_2_4 = ((15 + 6) - 10) * 4
# expression_value_2_5 = 17 / 2 % (2 * 3 ** 3)
# print(expression_value_2_1)
# print(expression_value_2_2)
# print(expression_value_2_3)
# print(expression_value_2_4)
# print(expression_value_2_5)
#
# # 3 Exercise
# anna_money = (11 - (1.5 * 3))
# print("remainder anna money:", anna_money, "rub")
#
# # 4 Exercise
# anna_apple = 2
# pol_apple = 5
# print("Paul:", pol_apple, "apple;", "Anna:", anna_apple, "apple")
#
# # 5 Exercise
# sample_input = int(input("Sample Input:"))
# print(sample_input, "суток" "=",
#       sample_input * 24, "часов", "=",
#       sample_input * 24 * 60, "минут", "=",
#       sample_input * 24 * 60 * 60, "секунд")
#
# # 6 Exercise
# weeks = 182 // 7
# print(weeks, "полных недель в 182 сутках")
#
# # 7 Exercise
# side_a, side_b = (input("Sample Input:").split())
# print("Sample Output: Можно отрезать", int((float(side_a) // 30) * (float(side_b) // 30)), "целых прямоугольников.")

# 8 Exercise
# sample_input = int(input("Sample Input:"))
# print(sample_input // (60 * 60), "час\n",
#       sample_input % (60 * 60) // 60, "минут\n",
#       sample_input % (60 * 60) % 60, "секунд")
#
# # 9 Exercise
# sample_input = int(input("Sample Input:"))
# print(sample_input // 100, "купюры по 100 рублей\n",
#       sample_input % 100 // 50, "купюры по 50 рублей\n",
#       sample_input % 100 % 50 // 10, "купюры по 10 рублей\n",
#       sample_input % 10, "купюры по 10 рублей"
#       )

# Exercise 10
#
# pole_height_h = 10
# upward_movement_x = 5
# downward_movement_y = 3
# # finish = pole_height_h // (upward_movement_x - downward_movement_y)
# # правильное решение
# finish = ((pole_height_h - 1) / upward_movement_x + 1 + 1)
# print(finish)

# Exercise 11
# long_km = 56
# speed_kmh_v = 60
# hour_t = 1
# minutes_m = 45
# speed_kmm = speed_kmh_v / 60
# time_m = hour_t * 60 + minutes_m
# distance_traveled = speed_kmm * time_m
# print(distance_traveled % long_km)
