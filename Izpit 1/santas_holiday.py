days = int(input())
type_of_room = ""
evaluation = ""
nights = days - 1
total_sum = 0
if nights < 10:
    if type_of_room == "room for one person":
        total_sum = nights * 18
    elif type_of_room == "apartment":
        total_sum = nights * 25 * 0.30
    elif type_of_room == "president apartment":
        total_sum = days * 35 * 0.10
elif 10 <= nights <=15:
    if type_of_room == "room for one person":
        total_sum = nights * 18
    elif type_of_room == "apartment":
        total_sum = nights * 25 * 0.35
    elif type_of_room == "president apartment":
        total_sum = days * 35 * 0.15
elif nights > 15:
    if type_of_room == "room for one person":
        total_sum = nights * 18
    elif type_of_room == "apartment":
        total_sum = nights * 25 * 0.50
    elif type_of_room == "president apartment":
        total_sum = days * 35 * 0.20
if evaluation == "positive":
    total_sum = total_sum * 0.25
elif evaluation == "negative":
    total_sum = total_sum * 0.90
print(total_sum)








