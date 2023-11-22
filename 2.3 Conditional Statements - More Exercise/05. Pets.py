import math
days = int(input())
foot_in_kg = int(input())
dog_foot_kg = float(input())
cat_foot_kg = float(input())
turtle_foot_kg = float(input())

price_foot_dog = days * dog_foot_kg
price_foot_cat = days * cat_foot_kg
price_foot_turtle = (days * turtle_foot_kg) / 1000

total_foot = math.ceil(price_foot_dog + price_foot_cat + price_foot_turtle)
diff = abs(total_foot - foot_in_kg)
if total_foot <= foot_in_kg:
    print(f"{diff} kilos of food left.")
else:
    print(f"{diff} more kilos of food are needed.")




