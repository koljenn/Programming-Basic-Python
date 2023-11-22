month = input()
nights = int(input())
total_studio_price = 0
total_apartment_price = 0
price_studio = 0
price_apart = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apart = 65
    if 7 < nights <= 14:
        price_studio = 0.95 * price_studio
    elif nights > 14:
        price_studio = 0.7 * price_studio
        price_apart = 0.9 * price_apart

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apart = 68.70
    if nights > 14:
        price_studio = 0.8 * price_studio
        price_apart = 0.9 * price_apart

elif month == "July" or month == "August":
    price_studio = 76
    price_apart = 77
    if nights > 14:
        price_apart = 0.9 * price_apart

total_apartment_price = nights * price_apart
total_studio_price = nights * price_studio

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")