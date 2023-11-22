# number_of_cats = int(input())
# group1 = 0
# group2 = 0
# group3 = 0
# food_per_day = 0
# price_food_per_day = 0
# for cats in range(number_of_cats):
#     grams_food = float(input())
#     if 100 <= grams_food < 200:
#         group1 += 1
#     elif 200 <= grams_food < 300:
#         group2 += 1
#     elif 300 <= grams_food <= 400:
#         group3 += 1
#     else:
#         grams_food = 0
#     food_per_day += grams_food
# price_food_per_day = food_per_day * 12.45 / 1000
# print(f'Group 1: {group1} cats.')
# print(f'Group 2: {group2} cats.')
# print(f'Group 3: {group3} cats.')
# print(f'Price for food per day: {price_food_per_day:.2f} lv.')

cats = int(input())

small = 0

big = 0

large = 0

total_food = 0

for i in range(cats):

    food = float(input())

    total_food += food

    if 100 <= food < 200:

        small += 1

    elif 200 <= food < 300:

        big += 1

    elif 300 <= food < 400:

        large += 1

price = total_food / 1000 * 12.45

print(f"Group 1: {small} cats.")

print(f"Group 2: {big} cats.")

print(f"Group 3: {large} cats.")

print(f"Price for food per day: {price:.2f} lv.")