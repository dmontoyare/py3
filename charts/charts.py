import matplotlib as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 40, 70]

    fig, ax = plt.subplotes()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()