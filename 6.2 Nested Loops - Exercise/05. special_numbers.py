number = int(input())
for current_number in range(1111, 9999 + 1):
    current_number_is_special = True
    current_number_as_string = str(current_number)
    for current_digit in current_number_as_string:
        # current_number не е специално, когато се дели на current_digit с остатък
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_number_is_special = False
            break
    if current_number_is_special:  # if current_number_is_special == True, current
        print(current_number_as_string, end=' ')


# num = int(input())
# for num1 in range(1, 10):
#     for num2 in range(1, 10):
#         for num3 in range(1, 10):
#             for num4 in range(1, 10):
#                 if num % num1 == num % num2 == num % num3 == num % num4 == 0:
#                     print(' ', end=f'{num1}{num2}{num3}{num4}')