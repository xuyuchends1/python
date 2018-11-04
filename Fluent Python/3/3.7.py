class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]

    def get(self,key,defalut=None):
        try:
            return self[key]
        except KeyError:
            return defalut

    def __setitem__(self, key, value):
        self[str(key)]=value

    def __contains__(self, key):
        return key in self.keys() or str(key) in  self.keys()


d=StrKeyDict0({'2':'two','4':'four'})
print(d['2'])
print(d[4])
# print(d[5])


d.get('2')
d.get(4)
d.get(1)