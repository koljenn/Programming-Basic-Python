cake_type = input()
purchased_cakes = int(input())
day = int(input())
price = 0
total_price = 0
discount = 0
if day <= 15:
    if cake_type == "Cake":
        price = 24
    elif cake_type == "Souffle":
        price = 6.66
    elif cake_type == "Baklava":
        price = 12.60
    total_price = price * purchased_cakes
elif day > 15:
    if cake_type == "Cake":
        price = 28.70
    elif cake_type == "Souffle":
        price = 9.80
    elif cake_type == "Baklava":
        price = 16.98
        total_price = price * purchased_cakes
if day <= 22:
    if 100 <= total_price <= 200:
        total_price = total_price * 0.15
    elif price > 200:
        total_price = total_price * 0.25
if day <= 15:
    total_price = total_price * 0.10
print(total_price)




