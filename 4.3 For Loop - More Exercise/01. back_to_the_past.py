money = float(input())
year = int(input())
age = 18

for i in range(1800, year + 1):
    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * age
    age += 1

if money < 0:
    print(f'He will need {abs(money):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')

# money = float(input())
# year = int(input())
# total_summ = money
# age = 18
# for year in range(1800, year + 1):
#     if year % 2 == 0:
#         total_summ -= 12000
#     else:
#         total_summ -= (12000 + (age * 50))
#     age += 1
# if total_summ >= 0:
#     print(f'Yes! He will live a carefree life and will have {total_summ:.2f} dollars left.')
# else:
#     print(f'He will need {abs(total_summ):.2f} dollars to survive.')