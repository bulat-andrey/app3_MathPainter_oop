class Canvas:

    def __init__(self, a, b, color):
        self.b = b
        self.a = a
        self.color = color

    def make(self):
        pass


class Rectangle:

    def __init__(self, x, y, a, b, color):
        self.color = color
        self.b = b
        self.a = a
        self.y = y
        self.x = x


    def draw(self, canvas):
        pass


class Square:

    def __init__(self, x, y, a, color):
        self.color = color
        self.a = a
        self.y = y
        self.x = x

    def draw(self, canvas):
        pass


