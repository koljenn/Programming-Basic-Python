import sys

n = int(input())

total_sum = 0
max_num = -sys.maxsize
for i in range(1, n + 1):
    curentNum = int(input())

    total_sum = total_sum + curentNum

    if curentNum > max_num:
        max_num = curentNum

sum = total_sum - max_num
if sum == max_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    diff = abs(sum - max_num)
    print(f"Diff = {diff}")
