init_hour = int(input())
init_minutes = int(input())
total_time = (init_hour * 60) + init_minutes + 15

hours =  total_time // 60
minutes= total_time % 60
if hours > 23:
    hours = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")


