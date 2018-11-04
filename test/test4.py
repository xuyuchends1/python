class U:
    def __init__(self, name):
        self.name = name
        self.p = []

    def _g(self, name):
        self.p.append(name)

    @property
    def revenge(self):
        print("10 year later...")
        for person in self.p:
            print("{0} stomps on {1}".format(self.name, person))


j = U("aa")
j.g("Tarek")
j.g("Bill")
j.revenge()
pass
