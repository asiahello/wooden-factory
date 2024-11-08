from src.boards import Board


def test_board():
    board = Board("MDF-700", type="MDF", density=700)
    assert board.weight(1000, 2000) == 18 * 700  # 18 mm * 1000 mm * 2000 mm * 700 kg/m^3

