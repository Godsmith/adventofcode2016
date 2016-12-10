class Container:
    def __init__(self, id):
        self.id = id
        self.cargo = set()

    def add_cargo(self, x):
        self.cargo.add(x)


class Bot(Container):
    def __init__(self, id):
        super().__init__(id)
        self.responsibilities = set()

    def empty(self):
        self.responsibilities = {x for x in self.cargo}
        out = max(self.cargo), min(self.cargo)
        self.cargo = set()
        return out


class Output(Container):
    pass
