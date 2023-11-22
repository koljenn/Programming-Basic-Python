number = int(input())
for numbers in range(0, number + 1, 2): # на степен 0,2,4,6,8,10...number
    print(2 ** numbers)
# или print(pow(2, numbers)) със from math import pow , но е float крайното число

# Втори вариант:
# number = int(input())
# for num in range(1, number + 1):
#     if num % 2 == 0:
#         print(2 ** num)
