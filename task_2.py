class Rational:
    def __init__(self, num=0, denom=0):
        a = num
        b = denom
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a + b != 0:
            num /= (a + b)
            denom /= (a + b)
        self._num = num
        self._denom = denom

    def fraction(self):
        print(int(self._num), '/', int(self._denom))

    def result(self):
        print(self._num / self._denom)


object1 = Rational(2, 5)
object1.fraction()
object1.result()