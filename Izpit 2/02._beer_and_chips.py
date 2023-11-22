import math

fen_name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beer_price = beer_count * 1.20
chips_price_per_count = beer_price * 0.45
chips_price = math.ceil(chips_price_per_count * chips_count)
total_sum = beer_price + chips_price
diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"{fen_name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{fen_name} needs {diff:.2f} more leva!")

