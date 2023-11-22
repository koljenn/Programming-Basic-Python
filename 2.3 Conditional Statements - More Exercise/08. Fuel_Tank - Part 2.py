fuel = input()
liters = float(input())
cart = input()
liter_price = 0

if cart == 'Yes':
    if fuel == 'Gas':
        liter_price = 0.85
    elif fuel == 'Diesel':
        liter_price = 2.21
    elif fuel == 'Gasoline':
        liter_price = 2.04
else:
    if fuel == 'Gas':
        liter_price = 0.93
    elif fuel == 'Diesel':
        liter_price = 2.33
    elif fuel == 'Gasoline':
        liter_price = 2.22

if 20 <= liters <= 25:
    liter_price *= 0.92
elif liters > 25:
    liter_price *= 0.9

print(f'{liter_price * liters:.2f} lv.')

# РЕШЕНИЕ
# С
# IF
# ELSE
# И
# ТЕРНАРЕН
# ОПЕРАТОР:
#
# fuel = input()
# liters = float(input())
# cart = input()
# liter_price = 0
#
# if fuel == 'Gas':
#     liter_price = 0.85 if cart == 'Yes' else 0.93
# elif fuel == 'Diesel':
#     liter_price = 2.21 if cart == 'Yes' else 2.33
# elif fuel == 'Gasoline':
#     liter_price = 2.04 if cart == 'Yes' else 2.22
#
# liter_price *= 0.92 if 20 <= liters <= 25 else 0.9 if liters > 25 else 1
#
# print(f'{liter_price * liters:.2f} lv.')
#
# И
# САМО
# С
# ТЕРНАРЕН
# ОПЕРАТОР:
#
# fuel = input()
# liters = float(input())
# cart = input()
#
# liter_price = (((0.85 if cart == 'Yes' else 0.93) if fuel == 'Gas' else
#                 (2.21 if cart == 'Yes' else 2.33) if fuel == 'Diesel' else
#                 (2.04 if cart == 'Yes' else 2.22) if fuel == 'Gasoline' else 0)
#                * (0.92 if 20 <= liters <= 25 else 0.9 if liters > 25 else 1))
#
# print(f'{liter_price * liters:.2f} lv.')
#
# РЕШЕНИЕ
# С
# КОЛЕКЦИЯ
# И
# ТЕРНАРЕН
# ОПЕРАТОР:
#
# fuel = input()
# liters = float(input())
# cart = input()
#
# info = {'Gas': {'Yes': 0.85, 'No': 0.93},
#         'Diesel': {'Yes': 2.21, 'No': 2.33},
#         'Gasoline': {'Yes': 2.04, 'No': 2.22}}
#
# liter_price = info[fuel][cart] * (0.92 if 20 <= liters <= 25 else 0.9 if liters > 25 else 1)
#
# print(f'{liter_price * liters:.2f} lv.')