budget = float(input())
count_statist = int(input())
price_clothing_one = float(input())

decor = budget * 0.10
all_clothes_price = count_statist * price_clothing_one

if count_statist > 150:
    all_clothes_price = all_clothes_price * 0.90
expenses = decor + all_clothes_price
diff = abs(expenses - budget)
if expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")

