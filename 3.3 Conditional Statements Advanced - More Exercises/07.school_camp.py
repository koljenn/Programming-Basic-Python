season = input()
gender = input()
students_count = int(input())
night_count = int(input())

price = 0
total_sum = 0

if season == "Winter":
    sport = "Gymnastics"
    if gender == "girls":
        price = 9.60

    elif gender == "boys":
        sport = "Judo"
        price = 9.60

    elif gender == "mixed":
        sport = "Ski"
        price = 10.00

if season == "Spring":
    sport = "Athletics"
    if gender == "girls":
        price = 7.20

    elif gender == "boys":
        sport = "Tennis"
        price = 7.20

    elif gender == "mixed":
        sport = "Cycling"
        price = 9.50

if season == "Summer":
    sport = "Volleyball"
    if gender == "girls":
        price = 15.00

    elif gender == "boys":
        sport = "Football"
        price = 15.00

    elif gender == "mixed":
        sport = "Swimming"
        price = 20.00
total_sum = students_count * price * night_count

if students_count >= 50:
    total_sum = total_sum * 0.50
if 20 <= students_count < 50:
    total_sum = total_sum * 0.85
if 10 <= students_count < 20:
    total_sum = total_sum * 0.95


print(f"{sport} {total_sum:.2f} lv.")
