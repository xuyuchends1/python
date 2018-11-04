from  array import array
import math

class Vector:
    typecode='d'
    def __init__(self,components):
        self._components=array(self.typecode,components)

    def __str__(self):
        return str(tuple(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)


    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __iter__(self):
        return iter(self._components)