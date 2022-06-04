from typing import List
from interpolation.spline import cubic_spline_interpolation_function
from data_structures.point import Point
from csv_utils.functionality import cubic_spline_data_plot, lagrange_data_plot

lagrange_data_plot("./data/Hel_yeah.csv", 7)
lagrange_data_plot("./data/100.csv", 5)

cubic_spline_data_plot("./data/Hel_yeah.csv", 70)
cubic_spline_data_plot("./data/100.csv", 50)
