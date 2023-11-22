# num = int(input())
# counter = 1
#
# for row in range(1, num + 1):
#     for col in range(row):
#         if counter > num:
#             break
#         print(' ', end=f'{counter}')
#         counter += 1
#     print()

number = int(input())
counter = 1
all_is_printed = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            all_is_printed = True
            break
    if all_is_printed: # all_is_printed == True
        break
    print()

