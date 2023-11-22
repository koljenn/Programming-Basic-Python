budget = float(input())
statist_count = int(input())
clothing_count = float(input())
decor_price = budget * 0.10
clothing_price = statist_count * clothing_count
if statist_count > 150:
    clothing_price = clothing_price * 0.90
all_sum = decor_price + clothing_price
diff = abs(all_sum - budget)
if all_sum <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")