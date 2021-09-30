import math


class Rational:
    def __init__(self, num=0, denom=1):
        try:
            if not denom:
                raise Exception
            self.__num = num / math.gcd(num, denom)
            self.__denom = denom / math.gcd(num, denom)
        except:
            print("Error")
            exit()

    def fraction(self):
        print(int(self.__num), '/', int(self.__denom))

    def result(self):
        print("result: ", self.__num / self.__denom)


object1 = Rational(2, 4)
object1.fraction()
object1.result()
