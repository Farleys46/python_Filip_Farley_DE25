from shape import Shape
from circle import Circle
from rectangle import Rectangle



circle1 = Circle(0, 4, 4)
rectangle1 = Rectangle(1, 2, "three", 3)
print(rectangle1.area)

print(rectangle1.perimeter)

print(rectangle1.is_square())