budget = float(input())
season = input()

type_car = 0
price_car = 0

if budget <= 100:
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.65
    print("Economy class")

elif 100 < budget <= 500:
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.80
    print("Compact class")
else:
    price_car = budget * 0.90
    type_car = "Jeep"
    print("Luxury class")

print(f"{type_car} - {price_car:.2F}")
