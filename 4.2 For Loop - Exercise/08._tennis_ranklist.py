from math import floor

tournaments_count = int(input())
start_points = int(input())
final_points = start_points
w_points = 0
f_points = 0
sf_points = 0
count_of_wins = 0

for tournament in range(1, tournaments_count + 1):
    stage_of_tournament = input()
    if stage_of_tournament == 'W':
        final_points += 2000
        w_points += 2000
        count_of_wins += 1
    if stage_of_tournament == 'F':
        final_points += 1200
        f_points += 1200
    if stage_of_tournament == 'SF':
        final_points += 720
        sf_points += 720

average_points = (w_points + f_points + sf_points) / tournaments_count
wins_percent = count_of_wins / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f'{wins_percent:.2f}%')