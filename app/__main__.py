from csv_utils.functionality import cubic_spline_data_plot, lagrange_data_plot, plot_data

plot_data("./data/WielkiKanionKolorado.csv")
plot_data("./data/MountEverest.csv")
plot_data("./data/SpacerniakGdansk.csv")

lagrange_data_plot("./data/WielkiKanionKolorado.csv", 5)
lagrange_data_plot("./data/MountEverest.csv", 5)
lagrange_data_plot("./data/SpacerniakGdansk.csv", 5)


cubic_spline_data_plot("./data/WielkiKanionKolorado.csv", 20)
cubic_spline_data_plot("./data/MountEverest.csv", 20)
cubic_spline_data_plot("./data/SpacerniakGdansk.csv", 20)
