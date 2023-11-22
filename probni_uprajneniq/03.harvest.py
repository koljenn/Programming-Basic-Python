# x = kv.m vineyard
import math

x = int(input())
# y = grapes for 1 kv.m
y = float(input())
# z = needed litres wine
z = int(input())
workers_count = int(input())

total_grape = x * y
wine = math.ceil(0.40 * total_grape / 2.5)
litres_wine = math.floor(wine - z)

litres_wine_per_person = math.ceil(litres_wine / workers_count)

if wine >= z:

    print(f"Good harvest this year! Total wine: {wine} liters.")
    print(f"{litres_wine} liters left -> {litres_wine_per_person} liters per person.")

else:
    print(f"It will be a tough winter! More {abs(litres_wine)} liters wine needed.")