from lab2 import Shape

class Circle(Shape):
    def __init__(self, x: int|float, y:int|float, radius: int|float):
        super().__init__(x, y)
        self.radius = radius
        
    @property
    def area(self):
        return 3.14159 * (self.radius * self.radius)
        
    @property
    def perimeter(self):
        return (2 * 3.14159) * self.radius
        
c1 = Circle(2, 3, 2)

c1.area()

    #def __repr__(self):
        #if isinstance(self, circle)