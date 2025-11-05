from shape import Shape
from numbers import Number
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as Circlepatch


class Circle(Shape):
    def __init__(self, x: int|float, y:int|float, radius: int|float):
        super().__init__(x, y)
        self.radius = radius
        
        #ErrorHandling.
        if not all(isinstance(value, Number) for value in (x, y)):
            raise TypeError(f"x and y values must be of type int or float")
        if not isinstance(radius, Number):
            raise TypeError(f"Radius must be a number and not {type(radius).__name__}")
        if radius <= 0:
            raise ValueError(f"Radius must be a positive number and not {radius}")
        
    @property
    def area(self):
        return 3.14159 * (self.radius * self.radius)
        
    @property
    def perimeter(self):
        return 2 * 3.14159 * self.radius
        
    def is_unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False

    def plot(self):
        fig, ax = plt.subplots()
        circ = Circlepatch((self.x, self.y), self.radius, edgecolor = "lightblue", facecolor = "red")
        ax.add_patch(circ)
        ax.set_xlim(self.x - self.radius * 2, self.x + self.radius * 2)
        ax.set_ylim(self.y - self.radius * 2, self.y + self.radius * 2)
        ax.set_aspect("equal")
        plt.grid(True)
        plt.title("Circle on Diagram")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
        