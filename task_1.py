class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("length and width must be of float type")
        if length < 0.0 or length > 20.00 or width < 0.0 or width > 20.0:
            raise ValueError("length and width must be in range (0, 20)")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def getter(self):
        return self.length, self.width

    def setter(self, length=1.0, width=1.0):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("length and width must be of float type")
        if length < 0.0 or length > 20.00 or width < 0.0 or width > 20.0:
            raise ValueError("length and width must be in range (0, 20)")
        self.length = length
        self.width = width
