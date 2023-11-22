fruits_price = float(input())
vegetables_price = float(input())
fruits_per_kg = int(input())
vegetables_per_kg = int(input())
fruits_sum = fruits_price * fruits_per_kg
vegetables_sum = vegetables_price * vegetables_per_kg
total_sum = (fruits_sum + vegetables_sum) / 1.94
print(f"{total_sum:.2f}")
