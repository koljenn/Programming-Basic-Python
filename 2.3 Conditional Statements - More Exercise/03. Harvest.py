from math import floor, ceil

surface_of_ground = int(input())
grape_for_sq_meter = float(input())
necessary_liters_of_vine = float(input())
workers_qt = float(input())

liters = surface_of_ground * grape_for_sq_meter
vine_liters = (liters * 0.40) / 2.5

diff = abs(vine_liters - necessary_liters_of_vine)
liters_per_person = diff / workers_qt

if vine_liters >= necessary_liters_of_vine:
    print(f"Good harvest this year! Total wine: {floor(vine_liters)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(liters_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
