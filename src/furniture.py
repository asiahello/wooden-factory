from boards import Board
from element import Element
from fittings import Fitting


from src.boards import BoardEnum


BOARDS = {
    BoardEnum.PLYWOOD: Board(name=BoardEnum.PLYWOOD, type="-", density=700),
    BoardEnum.MDF: Board(name=BoardEnum.MDF, type="-", density=1000),
    BoardEnum.CHIPBOARD: Board(name=BoardEnum.CHIPBOARD, type="-", density=600)
}


HINGE = Fitting(name="Hinge", weight=0.2)


class Cabinet:
    def __init__(self, width, height, type, board_name):
        self.width = width
        self.height = height
        # todo: zdefiniować typy mebli w enumie
        # todo: zmienić type na cabinet_type, bo type jest zarezerwowanym słowem kluczowym
        self.type = type
        self.board = BOARDS[board_name]
        self.elements = self._build_elements()

    # todo: zdefiniować enuma z materiałami
    # todo: podzielić na dwie klasy: HottyCabinet i VettyCabinet ?
    # todo: podzielić na mniejsze funkcje
    def _build_elements(self):
        elements = []
        if self.type == "hotty":
            horizontal_count = int(self.height / 50)
            vertical_count = int(self.width / 50)

            for _ in range(horizontal_count):
                elements.append(Element(width=self.width, height=50, board=self.board, fittings=[HINGE]))
            for _ in range(vertical_count):
                elements.append(Element(width=50, height=50, board=self.board, fittings=[]))
        elif self.type == "vetty":
            horizontal_count = int(self.width / 50)
            vertical_count = int(self.height / 50)

            for _ in range(vertical_count):
                elements.append(Element(width=50, height=self.height, board=self.board, fittings=[HINGE]))
            for _ in range(horizontal_count):
                elements.append(Element(width=self.width, height=50, board=self.board, fittings=[]))
        return elements

    def total_weight(self):
        return sum(element.weight() for element in self.elements)