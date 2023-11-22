students = int(input())

more_than_5 = 0
more_than_4 = 0
more_than_3 = 0
less_than_3 = 0
assessment = 0
result = 0
for i in range(1, students + 1):
    assessment = float(input())
    if assessment >= 5.00:
        more_than_5 += 1
    elif assessment >= 4.00:
        more_than_4 += 1
    elif assessment >= 3.00:
        more_than_3 += 1
    else:
        less_than_3 += 1
    result += assessment

diff = result / students

top_students = 100.0 * more_than_5 / students
four_students = 100.0 * more_than_4 / students
three_students = 100.0 * more_than_3 /students
two_students = 100.0 * less_than_3 / students

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {four_students:.2f}%")
print(f"Between 3.00 and 3.99: {three_students:.2f}%")
print(f"Fail: {two_students:.2f}%")
print(f"Average: {diff:.2f}")


