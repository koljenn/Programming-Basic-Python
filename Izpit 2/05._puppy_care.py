food_have = int(input())
all_gram_food = food_have * 1000

eaten_food = 0
total_food= 0
input = input()
while input != "Adopted":
    eaten_food = (input)
    eaten_food += 1
    total_food += eaten_food
    input()
    if total_food > all_gram_food:
        print(f"Food is not enough. You need {total_food - all_gram_food} grams more." )
    else:
        print(f"Food is enough! Leftovers: {all_gram_food - total_food} grams." )


