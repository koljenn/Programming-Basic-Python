number_of_loads = int(input())

price_bus = 0
price_truck = 0
price_train = 0

weight_sum = 0

# percent loads variables
p1_loads = 0
p2_loads = 0
p3_loads = 0

for i in range(1, number_of_loads + 1):
    weight_in_tons = int(input())

    if weight_in_tons <= 3:
        # vehicle = "microbus"
        price_bus += 200 * weight_in_tons
        p1_loads += weight_in_tons
    elif weight_in_tons <= 11:
        # vehicle = "truck"
        price_truck += 175 * weight_in_tons
        p2_loads += weight_in_tons

    else:
        # vehicle = "train"
        price_train += 120 * weight_in_tons
        p3_loads += weight_in_tons

    weight_sum += weight_in_tons

avg_price_total = (price_bus + price_truck + price_train) / weight_sum
avg_price_bus = p1_loads / weight_sum * 100
avg_price_truck = p2_loads / weight_sum * 100
avg_price_train = p3_loads / weight_sum * 100

print(f" {avg_price_total:.2f}")
print(f" {avg_price_bus:.2f}%")
print(f" {avg_price_truck:.2f}%")
print(f" {avg_price_train:.2f}%")