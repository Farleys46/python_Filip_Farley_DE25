from shape import Shape
from circle import Circle
from rectangle import Rectangle



circle1 = Circle(0, 4, 4)
rectangle1 = Rectangle(8, 8, 4, 2)

print(rectangle1.area)

print(rectangle1.perimeter)

print(rectangle1.is_square())

rectangle1.plot_rect()

circle1.__gt__(rectangle1)

circle1.plot_circ()