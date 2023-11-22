standard_tickets = 0
kid_tickets = 0
student_tickets = 0
movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_tickets in range(free_seats):
        current_ticket = input()
        if current_ticket == "End":
            break
        elif current_ticket == "student":
            student_tickets += 1
        elif current_ticket == "standard":
            standard_tickets += 1
        elif current_ticket == "kid":  # else
            kid_tickets += 1
        sold_seats += 1
    percent_full_hall = sold_seats / free_seats * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    movie_name = input()
total_tickets = student_tickets + standard_tickets + kid_tickets
percent_students_tickets = student_tickets / total_tickets * 100
percent_standard_tickets = standard_tickets / total_tickets * 100
percent_kid_tickets = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_students_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

# РЕШЕНИЕ
# С
# WHILE
# И
# FOR:
#
# standard_tickets = 0
# student_tickets = 0
# kid_tickets = 0
# movie = input()
#
# while movie != 'Finish':
#     seats = int(input())
#     counter = seats
#     for i in range(seats):
#         category = input()
#         if category == 'End':
#             counter = i
#             break
#         if category == 'student':
#             student_tickets += 1
#         elif category == 'standard':
#             standard_tickets += 1
#         else:
#             kid_tickets += 1
#
#     print(f'{movie} - {counter / seats * 100:.2f}% full.')
#     movie = input()
#
# total_tickets = standard_tickets + student_tickets + kid_tickets
# print(f'Total tickets: {total_tickets}')
# print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
# print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
# print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
#
# РЕШЕНИЕ
# С
# КОЛЕКЦИЯ:
#
# tickets = {"student": 0, "standard": 0, "kid": 0}
#
# while True:
#     movie = input()
#     if movie == 'Finish':
#         break
#     seats = int(input())
#     counter = 0
#     while counter != seats:
#         category = input()
#         if category == 'End':
#             break
#         tickets[category] += 1
#         counter += 1
#
#     print(f'{movie} - {counter / seats * 100:.2f}% full.')
#
# print(f'Total tickets: {sum(tickets.values())}')
# print(f'{tickets["student"] / sum(tickets.values()) * 100:.2f}% student tickets.')
# print(f'{tickets["standard"] / sum(tickets.values()) * 100:.2f}% standard tickets.')
# print(f'{tickets["kid"] / sum(tickets.values()) * 100:.2f}% kids tickets.')
#
# ИЛИ:
#
# tickets = {"student": 0, "standard": 0, "kid": 0}
#
# while True:
#     movie = input()
#     if movie == 'Finish':
#         break
#     seats = int(input())
#     counter = seats
#     for i in range(seats):
#         category = input()
#         if category == 'End':
#             counter = i
#             break
#         tickets[category] += 1
#
#     print(f'{movie} - {counter / seats * 100:.2f}% full.')
#
# print(f'Total tickets: {sum(tickets.values())}\n'
#       f'{tickets["student"] / sum(tickets.values()) * 100:.2f}% student tickets.\n'
#       f'{tickets["standard"] / sum(tickets.values()) * 100:.2f}% standard tickets.\n'
#       f'{tickets["kid"] / sum(tickets.values()) * 100:.2f}% kids tickets.')