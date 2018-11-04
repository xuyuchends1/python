class MarcoCommand:
    def __init__(self,commands):
        self.commands=list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()

def printa():
    print('a')

def printb():
    print('b')

m=MarcoCommand([printa,printb])
m()