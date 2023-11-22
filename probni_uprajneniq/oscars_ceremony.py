hall_price = int(input())
statuetes_price = hall_price * 0.70
catering_price = statuetes_price * 0.85
sound_price = catering_price / 2
all_price = hall_price + statuetes_price + catering_price + sound_price
print(f"{all_price:.2f}")