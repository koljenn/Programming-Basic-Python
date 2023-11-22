season = input()
kilometers_per_month = float(input())

all_kilometers = 0
price_km = 0
tax_vat = 0.90


if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat
    elif season == "Summer":
        price_km = 0.90
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat
    elif season == "Winter":
        price_km = 1.05
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat

if 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat
    elif season == "Summer":
        price_km = 1.10
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat
    elif season == "Winter":
        price_km = 1.25
        all_kilometers = (kilometers_per_month * price_km) * 4
        salary = all_kilometers * tax_vat

elif 10000 < kilometers_per_month <= 20000:
    price_km = 1.45
    all_kilometers = (kilometers_per_month * price_km) * 4
    salary = all_kilometers * tax_vat

print(f"{salary:.2f}")
