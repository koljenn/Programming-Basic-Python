party_price = float(input())
love_message = int(input())
wax_roses = int(input())
keychain = int(input())
caricature = int(input())
surprise = int(input())
all_party_sum = (love_message * 0.60) + (wax_roses * 7.20) + (keychain * 3.60) + (caricature * 18.20) + (surprise * 22.00)
article_sum = love_message + wax_roses + keychain + caricature + surprise
if article_sum >= 25:
    all_party_sum = all_party_sum * 0.65
final_price = all_party_sum - (all_party_sum * 0.10)
diff = abs(final_price - party_price)
if final_price >= party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")