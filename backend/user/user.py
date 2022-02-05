class User:
    def __init__(self, name, age, address, work, alone):
        self.name = name
        self.age = age
        self.address = address
        self.work = work
        self.alone = alone

    def category(self):
        return self.work

    def address(self):
        return self.address
