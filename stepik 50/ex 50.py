# Метаклассы. Объект type


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
print(A)
def method1(self):
    print(self.__dict__)


class B1:
    pass


class B2:
    pass


A = type("Point", (B1, B2), {"MAX_COORD": 100, "MIN_COORD": 0})
print(A.__mro__)

A = type("Point", (), {"MAX_COORD": 100, "MIN_COORD": 0, "method1": method1})
pt = A()
pt.method1()

A = type('Point', (), {'MAX_COORD': 100, 'method1': lambda self: print(self.MAX_COORD)})
pt = A()
pt.method1()