from fittings import Fitting
from boards import Board


class Element:
    depth = 18  # stała grubość dla każdego elementu

    def __init__(self, width: int, height: int, board: Board, fittings: list[Fitting]):
        self.width = width  # w mm
        self.height = height  # w mm
        self.board = board
        self.fittings = fittings

    def area(self):
        return self.width / 1000 * self.height / 1000  # powierzchnia w m^2

    def weight(self):
        plate_weight = self.area() * self.board.density * (self.depth / 1000)  # uwzględniamy grubość 18 mm
        fittings_weight = sum(fitting.weight for fitting in self.fittings)
        return plate_weight + fittings_weight