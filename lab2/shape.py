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
            raise TypeError(f"dx and dy must be numbers, not {type(dx)} and {type(dy)}")
        # Move position for the X and Y values. 
        else:
            self.x += dx
            self.y += dy
        
    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area < other.area

    def __gt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area > other.area
        
    def __le__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area <= other.area
        
    def __ge__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area >= other.area
        
        
    def __repr__(self):
        return(f"{self.__class__}x:{self.x}, y:{self.y}")
        
    def __str__(self):
        return(f"The {self.__class__.__name__} has the values X = {self.x}, Y = {self.y}")