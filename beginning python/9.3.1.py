def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class A:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, item):
        check_index(item)
        try:
            return self.changed[item]
        except KeyError:
            return self.start + self.step

    def __setitem__(self, key, value):
        check_index(key)
        self[key] = value


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.count = 0

    def __getitem__(self, item):
        self.count += 1
        return super().__getitem__(item)


cl = CounterList(range(10))
a = cl[5]
pass


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width = value
            self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError


a = Rectangle()
a.width = 5
a.size = 10

pass
