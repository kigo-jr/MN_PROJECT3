from turtle import color
from typing import List
from data_stuctures import Point
from interpolation import lagrange_interpolation
import matplotlib.pyplot as plt
import csv

def lagrange_data_plot(csv_file: str, split:int = 2):
    with open(csv_file, "r") as data:
        points: List[List[str]] = csv.reader(data)
        points = [[float(point[0]), float(point[1])] for point in points]
        points = [Point.from_list(point) for point in points]

        x = [point.x for point in points]
        y = [point.y for point in points]

        mid_points: int  = split - 2
        step: int = len(points) - 1
        if mid_points != 0:
            step = (len(points) - 1) // (mid_points + 1)

        split_points = x[0::step]

        f = lagrange_interpolation(points, split)

        plt.plot(x, y, label="pomiary")
        plt.plot([split_points[0] + i * 0.01 * (split_points[-1] - split_points[0]) for i in range(101)],\
                 [f(i) for i in [split_points[0] + i * 0.01 * (split_points[-1] - split_points[0]) for i in range(101)]],\
                 label="interpolacja Lagrange'a")
        plt.scatter(split_points, [f(i) for i in split_points], color="red", label="węzły interpolacji")
        plt.xlabel(r"$XD$")
        plt.ylabel(r"$\sum_{i=0}^{\inf}$")
        plt.title(csv_file)
        plt.legend()
        plt.grid()
        plt.show()