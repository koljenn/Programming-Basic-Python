budget = float(input())
vga_count = int(input())
cpu_count = int(input())
ram_count = int(input())

vga_price = vga_count * 250
cpu_price = cpu_count * (vga_price * 0.35)
ram_price = ram_count * (vga_price * 0.10)

total_sum = vga_price + cpu_price + ram_price
if vga_count > cpu_count:
    total_sum = total_sum * 0.85
diff = abs(budget - total_sum)
if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")



