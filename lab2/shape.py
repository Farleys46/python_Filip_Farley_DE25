"""Shape.py has the class "Shape" inside which is the parent class of rectangle and circle.
Here it also has area and perimeter but its defined in its child classes not here. 
The comparison operators are included where you can try "equal", "less than", "greater or equal to" etc.
For the equal checker, i decided to compare the area of two shapes in order to see if they are equal.
No matter the width, height etc. 
"""

from numbers import Number

# Creating main class "Shape" to store the base of the shapes like its x and y values.
class Shape:
    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y
        
    # Adding "@property" to area and perimeter and raising "NotImplemented" 
    # because the child classes will define them.
    @property
    def area(self):
        raise NotImplementedError(f"Child Class will have area")


    @property
    def perimeter(self):
        raise NotImplementedError(f"Child class will have perimeter")
    
    # Create "translate" method, to be able to move the x and y positions. You do this by "+" or "-" the x and y values
    def translate(self, dx:int|float, dy:int|float):
        if not (isinstance(dx, Number) and isinstance (dy, Number)): # Added ErrorHandling.
            raise TypeError(f"dx and dy must be numbers, not {type(dx)} and {type(dy)}")
        # Move position for the X and Y values. 
        else:
            self.x += dx
            self.y += dy
        
        
        
    # The equal check method only compares the area between 2 shapes. 
    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can only compare shapes and not {other}")
        else:
            return self.area == other.area

    # All comparison operators. All have ErrorHandling to make sure it compares 2 shapes and not int, string etc. 
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can only compare shapes and not {other}")
        else:
            return self.area < other.area

    def __gt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can only compare shapes and not {other}")
        else:
            return self.area > other.area
        
    def __le__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can only compare shapes and not {other}")
        else:
            return self.area <= other.area
        
    def __ge__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can only compare shapes and not {other}")
        else:
            return self.area >= other.area
        