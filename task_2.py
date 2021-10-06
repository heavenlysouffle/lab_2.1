import math


class Rational:
    def __init__(self, num=0, denom=1):
        if not isinstance(num, int) or not isinstance(denom, int):
            raise TypeError("numerator and denominator must be of integer type")
        if not denom:
            raise ZeroDivisionError
        self.__num = num // math.gcd(num, denom)
        self.__denom = denom // math.gcd(num, denom)

    def fraction(self):
        return f'{self.__num} / {self.__denom}'

    def result(self):
        return self.__num / self.__denom


object1 = Rational(2, 4)
print(object1.fraction())
print(object1.result)
