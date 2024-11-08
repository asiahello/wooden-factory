# Przykładowe dane materiałowe

# MDF = Board("MDF", density=700)  # gęstość 700 kg/m^3 dla płyty MDF
# HINGE = Fitting("Hinge", weight=0.2)  # przykładowy zawias o wadze 0.2 kg

from furniture import Cabinet
from pack import pack_elements
from src.visualizer import visualize_cabinet


def main():
    # Przykład tworzenia szafki typu hotty
    cabinet = Cabinet(width=1000, height=2000, type="hotty")
    print(f"Łączna waga szafki: {cabinet.total_weight()} kg")

    # Pakowanie elementów szafki
    packages = pack_elements(cabinet.elements)
    print(f"Szafka zapakowana w {len(packages)} paczek")

    # Wizualizacja
    visualize_cabinet(cabinet)


if __name__ == "__main__":
    main()