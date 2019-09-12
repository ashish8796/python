#Use of magic method __add__
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5,6)
second = Vector2D(6, 8)

result = first + second
print(result.x, result.y)
