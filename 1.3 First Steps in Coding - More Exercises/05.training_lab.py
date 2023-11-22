# w = float(input())
# numb_table_w = w // 1.2
# h = float(input())
# room_h = h-1
# numb_table = room_h // 0.70
# tables = numb_table * numb_table_w - 3
# print(f"{tables:.0f}")

w = float(input())
h = float(input())
if 3 <= h <= w <= 100:
    desks_per_row = int(((h * 100) - 100) / 70)
    rows = int((w * 100) / 120)
    stations = (desks_per_row * rows) - 3
print(stations)

# w = float(input()) * 100
# h = float(input()) * 100
#
# AISLE = 100
# seats_per_row = (h - AISLE) // 70
# rows = w // 120
#
# seats = seats_per_row * rows - 3
# print(int(seats))