# Class method - they are called by a class, which is passed to the cls parameter of the method.
# class method are marked with a classmethod decorator.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_lenght):
        return cls(side_lenght, side_lenght)


square = Rectangle.new_square(5) #Instantiating an instance of a class
print(square.calculate_area())