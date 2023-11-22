first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    odd_digit_sum = 0
    even_digit_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if odd_digit_sum == even_digit_sum:
        print(current_number, end = " ")

# Втори вариант:
# start_num = int(input())
# final_num = int(input())
#
# for num in range(start_num, final_num + 1):
#     sum_odd = 0
#     sum_even = 0
#     digit = num
#
#     for n in range(6):
#         if n % 2 == 0:
#             sum_odd += digit % 10
#         else:
#             sum_even += digit % 10
#         digit //= 10
#
#     if sum_odd == sum_even:
#         print(num, end=' ')

# РЕШЕНИЕ
# СЪС
# STR():
#
# start_num = int(input())
# final_num = int(input())
#
# for num in range(start_num, final_num + 1):
#     sum_odd = 0
#     sum_even = 0
#     current = str(num)
#     for n in range(len(current)):
#         digit = current[n]
#         if n % 2 == 0:
#             sum_odd += int(digit)
#         else:
#             sum_even += int(digit)
#
#     if sum_odd == sum_even:
#         print(num, end=' ')
#

