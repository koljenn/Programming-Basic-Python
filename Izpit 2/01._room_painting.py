import math

count_of_cans_of_paint = int(input()) # брой кутии боя
count_of_wallpaper_rolls = int(input()) # ролки тапети
gloves_per_count = float(input()) # цена на чифт ръкавици
brush_per_count = float(input()) # цена на една четка

paint_price = count_of_cans_of_paint * 21.50
wallpapers_price = count_of_wallpaper_rolls * 5.20
needed_gloves = math.ceil(count_of_wallpaper_rolls * 0.35)
needed_brush = math.floor(count_of_cans_of_paint * 0.48)
gloves_price = needed_gloves * gloves_per_count
brush_price = needed_brush * brush_per_count
sum_price = paint_price + wallpapers_price + gloves_price + brush_price
total_price = sum_price / 15
print(f"This delivery will cost {total_price:.2f} lv.")