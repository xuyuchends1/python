from array import array
import math


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __str__(self):
        return str(tuple(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, int):
            return self._components[item]
        else:
            msg = str(cls.__name__) + ' indices must be integers'
            raise TypeError(msg)

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
            msg = '{0} object has no attibute{1}'
            raise AttributeError(msg.format(cls.__name__, item))

    def __setattr__(self, key, value):
        cls = type(self)
        error = ""
        if len(key) == 1:
            if key in self.shortcut_names:
                error = 'readonly attibute {attr_name}'
            elif key.islower():
                error = "can't set attibute 'a' to 'z' in (cls_name)"

        if error:
            msg = error.format(cls_name=cls.__name__, attr_name=str(key))
            raise AttributeError(msg)
        super().__setattr__(key, value)


v = Vector([1, 2, 3, 4])
# v1=v[2:4]
# v2=v[2]
# v3=v['w']
v4 = v.x
v4.x = 10
print(v4.x)

pass
