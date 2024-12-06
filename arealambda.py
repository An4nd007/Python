area_square = lambda side: side ** 2

area_rectangle = lambda length, width: length * width

area_triangle = lambda base, height: 0.5 * base * height

side_of_square = 5
length_of_rectangle = 6
width_of_rectangle = 4
base_of_triangle = 8
height_of_triangle = 5

square_area = area_square(side_of_square)
rectangle_area = area_rectangle(length_of_rectangle, width_of_rectangle)
triangle_area = area_triangle(base_of_triangle, height_of_triangle)

print(f"Area of square: {square_area}")
print(f"Area of rectangle: {rectangle_area}")
print(f"Area of triangle: {triangle_area}")
