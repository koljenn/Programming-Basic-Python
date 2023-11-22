vacation_days = int(input())
# 63 workday play time
# 127 vacation play time
# 30000 max play yearly
work_days = 365 - vacation_days
play_time = work_days * 63 + vacation_days * 127
diff = abs(play_time - 30000)
hours = diff // 60
minutes = diff - hours * 60

if play_time > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
