from circle import circle
from rectangle import rectangle
from numbers import Number

class Shape:
    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y
        
    
    @property
    def area(self):
        raise NotImplementedError(f"Child Class will have area")


    @property
    def perimeter(self):
        raise NotImplementedError(f"Child class will have perimeter")
    
    def translate(self, dx:int|float, dy:int|float):
        if not (isinstance(dx, Number) and isinstance (dy, Number)):
            raise TypeError(f"dx and dy needs to be a number and not of type {type(dx) and type(dy)}")
        # Move position for the X and Y values. 
        else:
            self.x += dx
            self.y += dy
        
    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented(f"You need to compare 2 shapes")
        else:
            return self.area == other.area




circle1 = Shape(1, 3)

circle1.translate(3, 2)