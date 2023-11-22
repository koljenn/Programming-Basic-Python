num = int(input())
bonus = 0
if num <= 100:
    bonus = 5
elif num <= 1000:
    bonus = num * 0.20
else:
    bonus = num * 0.10
if num % 2 == 0:
    bonus = bonus + 1
elif num % 10 == 5:
    bonus = bonus + 2
total_point = num + bonus
print(bonus)
print(total_point)



