import math
magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolia_price = magnolia_count * 3.25
hyacinth_price = hyacinth_count * 4
rose_price = rose_count * 3.50
cactus_price = cactus_count * 8

total_price = (magnolia_price + hyacinth_price + rose_price + cactus_price) * 0.95
diff = abs(total_price - gift_price)
if total_price < gift_price:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
else:
    print(f"She is left with {math.floor(diff)} leva.")




