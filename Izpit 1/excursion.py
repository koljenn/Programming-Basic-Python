people_count = int(input())
night_count = int(input())
cart_count = int(input())
ticket_count = int(input())
night_price = night_count * 20
cart_price = cart_count * 1.60
ticket_price = ticket_count * 6
personal_sum = night_price + cart_price + ticket_price
total_sum = personal_sum * people_count * 1.25
print(f"{total_sum:.2f}")
