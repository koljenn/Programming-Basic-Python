game_step = int(input())

result = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
for i in range(1, game_step + 1):
    value = int(input())
    if 0 <= value <= 50:
        if value < 10:
            value1 = value * 0.2
            n1 += 1
        elif value < 20:
            value1 = value * 0.3
            n2 += 1
        elif value < 30:
            value1 = value * 0.4
            n3 += 1
        elif value < 40:
            value1 = 50
            n4 += 1
        else:
            value1 = 100
            n5 += 1
        result += value1
    else:
        result /= 2
        n6 += 1
print(f"{result:.2f}")

from_0_to_9 = n1 * 1.0 / game_step * 100
print(f"From 0 to 9: {from_0_to_9:.2f}%")
from_10_to_19 = n2 * 1.0 / game_step * 100
print(f"From 10 to 19: {from_10_to_19:.2f}%")
from_20_to_29 = n3 * 1.0 / game_step * 100
print(f"From 20 to 29: {from_20_to_29:.2f}%")
from_30_to_39 = n4 * 1.0 / game_step * 100
print(f"From 30 to 39: {from_30_to_39:.2f}%")
from_40_to_50 = n5 * 1.0 / game_step * 100
print(f"From 40 to 50: {from_40_to_50:.2f}%")
invalid_numbers = n6 * 1.0 / game_step * 100
print(f"Invalid numbers: {invalid_numbers:.2f}%")






