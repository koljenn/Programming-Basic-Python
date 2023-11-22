some_text = input()
sum_of_points = 0
for letter in some_text: # text_lenght = len(some_text)
    if letter == "a":
        sum_of_points += 1
    elif letter == "e":
        sum_of_points += 2
    elif letter == "i":
        sum_of_points += 3
    elif letter == "o":
        sum_of_points += 4
    elif letter == "u":
        sum_of_points += 5
print(sum_of_points)

# some_text = input()
# sum_of_points = 0
# lenght_of_some_text = len(some_text)
# for current_index in range(0, lenght_of_some_text):  # range(lenght_of_some_text)
#     if some_text[current_index] == "a":
#         sum_of_points += 1  # sum_of_points = sum_of_points + 1
#     elif some_text[current_index] == "e":
#         sum_of_points += 2
#     elif some_text[current_index] == "i":
#         sum_of_points += 3
#     elif some_text[current_index] == "o":
#         sum_of_points += 4
#     elif some_text[current_index] == "u":
#         sum_of_points += 5
# print(sum_of_points)
