class Point:
    default_color = "red" #class atribute

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point({self.x}, {self.y})")
Point.default_color = "Blue" #changing the color of the class atribute
point = Point(2, 5)
print(point.default_color) #calling 
print(Point.default_color)