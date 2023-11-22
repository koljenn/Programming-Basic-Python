period = int(input())
treated = 0
untreated = 0
doctors = 7

for i in range(1, period + 1):
    patients = int(input())
    if untreated > treated and i % 3 == 0:
        doctors += 1
    if patients > doctors:
        treated += doctors
        untreated += patients - doctors
    else:
        treated += patients

print(f'Treated patients: {treated}.\nUntreated patients: {untreated}.')

# period = int(input())
# docs = 7
# yes = 0
# no = 0
# if period == 0:
#     exit()
# for day in range(1, period + 1):
#     people = int(input())
#     if day % 3 == 0:
#         if no > yes:
#             docs += 1
#     if docs >= people:
#         yes += people
#     else:
#         yes += docs
#         no += people - docs
# print(f"Treated patients: {yes}.")
# print(f"Untreated patients: {no}.")