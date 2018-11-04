import collections

class StrKeyDict0(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,defalut=None):
        try:
            return self[key]
        except KeyError:
            return defalut