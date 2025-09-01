import math
import matplotlib.pyplot as plt


# Exemple de graphique en ligne avec annotations
def plot_grid():
    labels = ["note 1", "note 2", "note 3", "note 4", "note 5", "note 6"]
    mathematique = [10, 8, 14, 18, 11, 16]
    physique = [12, 4, 18, 15, 2, 13]
    chimie = [14, 6, 12, 19, 9, 17]

    plt.ylim(0, 20)

    plt.plot(labels, mathematique, marker="o", label="Mathématique")
    plt.plot(labels, physique, marker="o", label="Physique")
    plt.plot(labels, chimie, marker="o", label="Chimie")
    plt.xlabel("Examen")
    plt.ylabel("Notes")
    plt.title("Notes de l'année 2023")

    plt.legend()

    for i in range(len(labels)):
        plt.text(
            labels[i],
            mathematique[i],
            str(mathematique[i]),
            ha="left",
            va="top",
            bbox=dict(facecolor="white", alpha=0.5),
        )
        plt.text(labels[i], physique[i], str(physique[i]), ha="left", va="top", bbox=dict(facecolor="white", alpha=0.5))
        plt.text(labels[i], chimie[i], str(chimie[i]), ha="left", va="top", bbox=dict(facecolor="white", alpha=0.5))


# Exemple de graphique en ligne d'une courbe sinusoîde amortie
def plot_xy():
    nb_points = 200
    xmin = -8 * math.pi
    xmax = 8 * math.pi
    interval = xmax - xmin
    step = interval / nb_points
    yvalues = []
    xvalues = []
    for idx in range(nb_points):
        x = xmin + step * idx
        # y = math.sin(x) * math.exp(-0.1*abs(x))
        y = math.sin(x) / x if x != 0 else 1  # Gérer le cas où x est 0 pour éviter la division par zéro
        xvalues.append(x)
        yvalues.append(y)

    fig, ax = plt.subplots()
    ax.plot(xvalues, yvalues)


# Exemple de graphique en camembert
def plot_pie():
    labels = ["0 - 18 ans", "18 - 25 ans", "25 - 40 ans", "40 - 65 ans", "65 ans et +"]
    percent = [15, 25, 35, 20, 5]
    plt.pie(percent, labels=labels)


# Exemple de graphique en barres
def plot_bar():
    labels = ["0 - 18 ans", "18 - 25 ans", "25 - 40 ans", "40 - 65 ans", "65 ans et +"]
    percent = [15, 25, 35, 20, 5]
    plt.bar(labels, percent, color=["red", "blue", "green", "orange", "purple"])


plot_xy()
# plot_grid()
# plot_pie()
# plot_bar()

plt.grid()
plt.show()
