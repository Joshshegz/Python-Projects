#Creating Classes iN PYTHON

class Point:
    default_color = "red"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(10  ,20 )
    
    def __eq__(self, other ):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    
    def __add__(self, other):
        return self.x + other.x and self.y + other.y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
point = Point(1, 2)
# print(type(point)) 

# print(isinstance(point, Point))
# print(point.x)
 
# point.draw()
# another = Point(10, 3)
# another.draw()

# print(Point.default_color)
# print(point.default_color )

#CLASS METHODS
point = Point.zero()
point.draw()

#MAGIC METHODS 
other = Point(1, 2)
print(point == other)
print(point < other)
print(point + other)