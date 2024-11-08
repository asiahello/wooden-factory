class Board:
    thickness = 18  # stala grubość dla każdej płyty

    def __init__(self, name: str, type: str, density: float):
        self.name = name
        # todo: zmienic type na material, bo type jest zarezerwowanym słowem kluczowym
        # todo: zdefiniować typy matriałów: np MDF, plywood w enumie
        self.type = type
        self.density = density  # w kg/m^3

    def weight(self, width: int, height: int):
        return width / 1000 * height / 1000 * self.density * self.thickness / 1000