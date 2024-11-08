class Fitting:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # todo: zdefiniować jednostki wagi

    def __repr__(self):
        return f'Okucie({self.name}, {self.weight}g)'