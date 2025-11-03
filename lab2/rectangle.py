from shape import Shape
from numbers import Number 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as Rectangleplot, Circle as Circleplot

class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width
        
        if not all(isinstance(value, Number) for value in (x, y, height, width)):
            raise TypeError(f"values must be of type int or float")
        if height <= 0 or width <= 0:
            raise ValueError(f"Height and width must be positive and not {height, width}")

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

    #    
    def plot(self):
        fig, ax = plt.subplots(Rectangle)