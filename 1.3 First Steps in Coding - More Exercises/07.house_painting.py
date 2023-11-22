# x = float(input())
# y = float(input())
# h = float(input())
#
# side_wall = x * y
# windows = 1.5 * 1.5
# double_side_wall = (2 * side_wall) - (2 * windows)
# back_wall = x * x
# enter = 1.2 * 2
# back_and_front_wall = (2 * back_wall) - enter
# wall_sum = double_side_wall + back_and_front_wall
# green_paint = wall_sum / 3.4
# print(f"{green_paint:.2f}")
#
# roof_rectangle = 2 * (x * y)
# roof_triangle = 2 * (x * h / 2)
# roof_sum = roof_rectangle + roof_triangle
# red_paint = roof_sum / 4.3
# print(f"{red_paint:.2f}")

x = float(input())
y = float(input())
h = float(input())

# needed green paint
front = x * x - 2 * 1.2
back = x * x
aside = 2 * (x * y - 1.5 * 1.5)
total_metres_green = front + back + aside
green_paint = total_metres_green / 3.4

# needed red paint
sides = 2 * x * y
triangles = x * h
total_metres_red = sides + triangles
red_paint = total_metres_red / 4.3

print(round(green_paint, 2))
print(round(red_paint, 2))
