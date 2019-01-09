from matplotlib import pyplot

#prepare data
machine_counts = [18, 4, 2]

#prepare labels
machine_names = ["MAC", "PC", "Linux"]

#draw pie
pyplot.pie(machine_counts, labels=machine_names, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.title("PC vs MAC vs Linux usage")

pyplot.axis("equal")

pyplot.show()