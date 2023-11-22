first = int(input())
seconds = int(input())
third = int(input())

total_time = first + seconds + third

minutes = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

