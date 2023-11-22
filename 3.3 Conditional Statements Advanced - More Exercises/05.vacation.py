budget = float(input())
season = input()

location = 0
place = ""
price = 0

if budget <= 1000:
    if season == "Summer":
        location = "Alaska"
        place = "Camp"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        place = "Camp"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    if season == "Summer":
        location = "Alaska"
        place = "Hut"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        place = "Hut"
        price = budget * 0.60

elif budget > 3000:
    if season == "Summer":
        location = "Alaska"
        place = "Hotel"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        place = "Hotel"
        price = budget * 0.90

print(f"{location} - {place} - {price:.2f}")