class Rectangle:
    def __init__(self, length=1, width=1):
        self._width = width
        self._length = length

    def perimeter(self):
        print("perimeter:", 2 * (self._length + self._width))

    def area(self):
        print("area:", self._length * self._width)

    def getter(self):
        return self._width, self._length

    def setter(self, x = 1, y = 1):
        try:
            float(x)
            float(y)
            if 0.0 < x < 20.0 and 0.0 < y < 20.0:
                self._length = x
                self._width = y
            else:
                print("length and width are each floating-point numbers larger than 0.0 and less than 20.0")
                exit()
        except ValueError:
            print("error")
            