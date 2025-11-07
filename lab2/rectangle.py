from shape import Shape
from numbers import Number 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as Rectanglepatch

#Creating class Rectangle, with passive x and y values. If the user dont input them they will be (0,0,1,1)
class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        self.width = width
        self.height = height
        
        # ErrorHandling, If not these values have a number as input they will raise suitable Errors. 
        if not all(isinstance(value, Number) for value in (x, y)):
            raise TypeError(f"x and y values must be of type int or float")
        if not all(isinstance(value, Number) for value in (width, height)):
            raise TypeError(f"Width and Height must be numbers and not {width, height}")
        if height <= 0 or width <= 0:
            raise ValueError(f"Width and Height must be positive and not {width, height}")
    
    # Set area and perimeter as @property
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
    #Also took inspo from this youtube video: https://www.youtube.com/watch?v=kmA6P4vjuaI
    def plot(self):
        corner_x = self.x - self.width / 2 # Had to look up how to change center position from bottom left
        corner_y = self.y - self.height / 2 # Could not find site so took help from LLM (Chatgpt)
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
    
    
    # Moved the overload of repr and str into each subclass to be able to show Radius and Width, Height    
    def __repr__(self):
        return(f"{self.__class__}x:{self.x}, y:{self.y}, w:{self.width}, h:{self.height}")
        
    def __str__(self):
        return(f"The {self.__class__.__name__} has the values X = {self.x}, Y = {self.y}, Width = {self.width} and Height = {self.height}")