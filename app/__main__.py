from typing import List
from csv_utils.functionality import cubic_spline_data_plot, lagrange_data_plot, plot_data

plot_data("./data/WielkiKanionKolorado.csv")
plot_data("./data/MountEverest.csv")
plot_data("./data/SpacerniakGdansk.csv")

no_points: List[int] = [4, 10, 14]

print("Równomierny dobór węzłów - Lagrange")
for n in no_points:

    lagrange_data_plot("./data/WielkiKanionKolorado.csv", n)
    lagrange_data_plot("./data/MountEverest.csv", n)
    lagrange_data_plot("./data/SpacerniakGdansk.csv", n)

print("Losowy dobór węzłów - Lagrange")
for n in no_points:

    lagrange_data_plot("./data/WielkiKanionKolorado.csv", n, False)
    lagrange_data_plot("./data/MountEverest.csv", n, False)
    lagrange_data_plot("./data/SpacerniakGdansk.csv", n, False)

no_points = [10, 20, 50, 100]

print("Równomierny dobór węzłów - splajny")
for n in no_points:
    cubic_spline_data_plot("./data/WielkiKanionKolorado.csv", n)
    cubic_spline_data_plot("./data/MountEverest.csv", n)
    cubic_spline_data_plot("./data/SpacerniakGdansk.csv", n)

print("Losowy dobór węzłów - splajny")
for n in no_points:
    cubic_spline_data_plot("./data/WielkiKanionKolorado.csv", n, False)
    cubic_spline_data_plot("./data/MountEverest.csv", n, False)
    cubic_spline_data_plot("./data/SpacerniakGdansk.csv", n, False)
