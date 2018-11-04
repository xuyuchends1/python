import math
import itertools

class Vector:
    def __init__(self,x,y):
        self.__x=float(x)
        self.__y=float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __abs__(self):
        return math.sqrt((sum(x*x for x in self)))

    # -
    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        pairs=itertools.zip_longest(self,other, fillvalue=0.0)
        return Vector(a+b for a,b in pairs)

a=Vector(1,2)
b=abs(a)

v1=Vector(3,4)
v2=Vector(6,7)
v3=v1+v2


pass