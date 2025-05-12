import matplotlib.pyplot as plt

def bar_chart(x, y, title, x_label, y_label, rotate_x=False, figsize=(10,6)):
    plt.figure(figsize=figsize)
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if rotate_x:
        plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def line_chart(x, y1, y2=None, title="", x_label="", y_label=""):
    plt.figure(figsize=(10,6))
    plt.plot(x, y1, marker='o', label=y_label or "Series1")
    if y2 is not None:
        plt.plot(x, y2, marker='o', label="Series2")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.tight_layout()
    plt.show()
