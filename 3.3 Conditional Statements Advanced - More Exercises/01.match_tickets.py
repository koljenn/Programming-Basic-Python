budget = float(input())
category = input("")
people = int(input())
price_vip = 499.99
price_normal = 249.99
transport = 0
price_all_tickets = 0

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25

budget = budget - transport

if category == "Normal":
    price_all_tickets = people * price_normal
elif category == "VIP":
    price_all_tickets = people * price_vip

if budget >= price_all_tickets:
    print(f"Yes! You have {(budget - price_all_tickets):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price_all_tickets - budget):.2f} leva.")

















