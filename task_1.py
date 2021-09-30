class Rectangle:
    def __init__(self):
        self.length = 1
        self.width = 1

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def getter(self):
        return self.length, self.width

    def setter(self, length=1, width=1):
        try:
            if type(length) is not float or type(width) is not float:
                raise Exception
            if length < 0.0 or length > 20.00 or width < 0.0 or width > 20.0:
                raise Exception
            self.length = length
            self.width = width
        except:
            print("Error: values should be floating-point numbers in range (0, 20)")
            exit()
