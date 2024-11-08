import matplotlib.pyplot as plt

def visualize_cabinet(cabinet):
    fig, ax = plt.subplots()
    y_offset = 0

    for element in cabinet.elements:
        rect = plt.Rectangle((0, y_offset), element.width / 10, element.height / 10, fill=True, edgecolor="black")
        ax.add_patch(rect)
        y_offset += element.height / 10 if element.width > element.height else 0

    ax.set_xlim(0, max(element.width for element in cabinet.elements) / 10)
    ax.set_ylim(0, y_offset)
    plt.gca().invert_yaxis()
    plt.show()