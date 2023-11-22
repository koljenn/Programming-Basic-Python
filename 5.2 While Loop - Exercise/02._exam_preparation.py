poor_grades = int(input()) # Слаби оценки

input_line = input()
sum_all_grades = 0 # сума_всички_оценки
count_grades = 0 # брои_оценки
last_problem = "" # последен_проблем
poor_grades_count = 0 # брой_лоши_оценки
while input_line != "Enough":
    last_problem = input_line
    current_grade = int(input()) # текуща_оценка
    if current_grade <= 4:
        poor_grades_count += 1
    count_grades += 1
    sum_all_grades += current_grade

    if poor_grades_count >= poor_grades:
        break

    input_line = input()

if poor_grades_count == poor_grades:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    avg_grade = sum_all_grades / count_grades # средна_оценка = сума_всички_оценки / брой_оценки
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")
