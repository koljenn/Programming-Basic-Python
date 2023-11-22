type_flowers = input()
count_flowers = int(input())
budget = int(input())
sum = 0
if type_flowers == "Roses":
    sum = count_flowers * 5
    if count_flowers > 80:
        sum = sum * 0.90
elif type_flowers == "Dahlias":
    sum = count_flowers * 3.80
    if count_flowers > 90:
        sum = sum * 0.85
elif type_flowers == "Tulips":
    sum = count_flowers * 2.80
    if count_flowers > 80:
        sum = sum * 0.85
elif type_flowers == "Narcissus":
    sum = count_flowers * 3
    if count_flowers < 120:
        sum = sum * 1.15
elif type_flowers == "Gladiolus":
    sum = count_flowers * 2.50
    if count_flowers < 80:
        sum = sum * 1.20
diff = abs(budget - sum)
if sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
