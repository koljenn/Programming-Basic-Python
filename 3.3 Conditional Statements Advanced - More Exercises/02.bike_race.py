juniors = int(input())
seniors = int(input())
trace = input("")
juniors_tax = 0
seniors_tax = 0
sum = 0
if trace == "trail":
    juniors_tax = juniors * 5.50
    seniors_tax = seniors * 7
    sum = (juniors_tax + seniors_tax) * 0.95
elif trace == "cross-country":
    juniors_tax = juniors * 8
    seniors_tax = seniors * 9.50
    sum = (juniors_tax + seniors_tax) * 0.95
    if juniors + seniors >=50:
        sum = sum * 0.75
elif trace == "downhill":
    juniors_tax = juniors * 12.25
    seniors_tax = seniors * 13.75
    sum = (juniors_tax + seniors_tax) * 0.95

elif trace == "road":
    juniors_tax = juniors * 20.00
    seniors_tax = seniors * 21.50
    sum = (juniors_tax + seniors_tax) * 0.95

print(f"{sum:.2f}")
