from lab2 import Shape 

class Circle(Shape):
    def __init__(self, radius: int|float, area: int|float, perimeter: int|float)
    
    def radius(self, radius: int|float):
        self.radius = radius
        
    @property
    def area(self, area: int|float):
        self.area = area
        area = 3.14159 * (self.radius * self.radius)
        
    @property
    def perimeter(self, perimeter: int|float):
        self.perimeter = perimeter
        perimeter = (2 * 3.14159) * self.radius


    def __repr__(self):
        if isinstance(self, circle)