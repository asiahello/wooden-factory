from furniture import Cabinet
from pack import pack_elements

# from src.visualizer import visualize_cabinet

def main():
    # Przykład tworzenia szafki typu hotty
    cabinet = Cabinet(width=1000, height=2000, type="hotty", board_name="plywood")
    print(f"Łączna waga szafki: {cabinet.total_weight()} kg")
    print(f"materiał płyty: {cabinet.board} ")
    # Pakowanie elementów szafki
    packages = pack_elements(cabinet.elements)
    print(f"Szafka zapakowana w {len(packages)} paczek")

    # Wizualizacja
    # visualize_cabinet(cabinet)


if __name__ == "__main__":
    main()