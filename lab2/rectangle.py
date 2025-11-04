from shape import Shape
from numbers import Number 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as Rectanglepatch

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        
        if not all(isinstance(value, Number) for value in (x, y, width, height)):
            raise TypeError(f"values must be of type int or float")
        if height <= 0 or width <= 0:
            raise ValueError(f"Width and Height must be positive and not {width, height}")

    @property
    def area(self):
        return self.height * self.width
    
    @property
    def perimeter(self):
        return (self.height * 2) + (self.width * 2)
    
    def is_square(self) -> bool:
        if self.height == self.width:
            return True
        else:
            return False

    #Plot help from this site: https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
    
    def plot(self):
        corner_x = self.x - self.width / 2 # Since it is the bottom left corner that starts the plot,
        corner_y = self.y - self.height / 2 # i changed it to be the center position.
        fig, ax = plt.subplots()
        rect = Rectanglepatch((corner_x, corner_y), self.width, self.height, edgecolor="lightblue", facecolor = "red")
        ax.add_patch(rect)
        ax.set_xlim(self.x - self.width * 2, self.x + self.width * 2)
        ax.set_ylim(self.y - self.height * 2, self.y + self.height * 2)
        ax.set_aspect("equal")
        plt.grid(True)
        plt.title("Rectangle on Diagram")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()