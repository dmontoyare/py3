import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["Daniel", "Pedro", "Juan"]
    values = [200, 40, 70]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(".png")
    plt.show()
    plt.close()