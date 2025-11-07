from shape import Shape
from numbers import Number
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as Circlepatch

# Create class "Circle" with passive positions at (0, 0, 1) so you can call "CircleX = Circle()"
# Without any inputs and it will give you a unit circle.
class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius
        
        #ErrorHandling.
        if not all(isinstance(value, Number) for value in (x, y)):
            raise TypeError(f"x and y values must be of type int or float")
        if not isinstance(radius, Number):
            raise TypeError(f"Radius must be a number and not {type(radius).__name__}")
        if radius <= 0:
            raise ValueError(f"Radius must be a positive number and not {radius}")
        
        
        # Calculate area and perimeter on circle. 
    @property
    def area(self):
        return 3.14159 * (self.radius * self.radius)
        
    @property
    def perimeter(self):
        return 2 * 3.14159 * self.radius
        
        
        
        # If the circle has center position on origo and radius is equal to 1, then its a unit circle
    def is_unit_circle(self) -> bool:
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return True
        else:
            return False
        
        
        # Took help from this site to plot: https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
        # Also this yt video: https://www.youtube.com/watch?v=kmA6P4vjuaI
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
        
        # Moved the overload of repr and str into each subclass to be able to show Radius and Width, Height
    def __repr__(self):
        return(f"{self.__class__}x:{self.x}, y:{self.y}, r:{self.radius}")
        
    def __str__(self):
        return(f"The {self.__class__.__name__} has the values X = {self.x}, Y = {self.y}, Radius = {self.radius}")