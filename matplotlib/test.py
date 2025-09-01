import matplotlib.pyplot as plt

# Exemple de graphique en ligne avec annotations
"""
labels = ["note 1", "note 2", "note 3", "note 4", "note 5", "note 6"]
mathematique = [10, 8, 14, 18, 11, 16]
physique = [12, 4, 18, 15, 2, 13]
chimie = [14, 6, 12, 19, 9, 17]

plt.ylim(0, 20)

plt.plot(labels, mathematique, marker='o', label="Mathématique")
plt.plot(labels, physique, marker='o', label="Physique")
plt.plot(labels, chimie, marker='o', label="Chimie")
plt.xlabel("Examen")
plt.ylabel("Notes")
plt.title("Notes de l'année 2023")

plt.legend()
plt.grid()

for i in range(len(labels)):
    plt.text(labels[i], mathematique[i], str(mathematique[i]), ha='left', va='top', bbox=dict(facecolor='white', alpha=0.5))
    plt.text(labels[i], physique[i], str(physique[i]), ha='left', va='top', bbox=dict(facecolor='white', alpha=0.5))
    plt.text(labels[i], chimie[i], str(chimie[i]), ha='left', va='top', bbox=dict(facecolor='white', alpha=0.5))
"""

labels = ["0 - 18 ans", "18 - 25 ans", "25 - 40 ans", "40 - 65 ans", "65 ans et +"]
percent=[15, 25, 35, 20, 5]

# Exemple de graphique en camembert
# plt.pie(percent, labels=labels)

# Exemple de graphique en barres
plt.bar(labels, percent, color=['red', 'blue', 'green', 'orange', 'purple'])

plt.show()