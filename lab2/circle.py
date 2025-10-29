from shape import Shape

class Circle(Shape):
    def __init__(self, x: int|float, y:int|float, radius: int|float):
        super().__init__(x, y)
        self.radius = radius
        
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

    #def __repr__(self):
        #if isinstance(self, circle)