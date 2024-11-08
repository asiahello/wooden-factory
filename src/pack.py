class Package:
    MAX_WEIGHT = 20  # maksymalna waga paczki w kg

    def __init__(self):
        self.items = []
        self.current_weight = 0

    def add_item(self, item):
        item_weight = item.weight()
        if self.current_weight + item_weight <= self.MAX_WEIGHT:
            self.items.append(item)
            self.current_weight += item_weight
            return True
        return False

def pack_elements(elements):
    packages = []
    current_package = Package()

    for element in elements:
        if not current_package.add_item(element):
            packages.append(current_package)
            current_package = Package()
            current_package.add_item(element)
    packages.append(current_package)  # dodaj ostatnią paczkę
    return packages