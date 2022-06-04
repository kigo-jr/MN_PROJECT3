from typing import List
from data_structures import Point
from interpolation import lagrange_interpolation, cubic_spline_interpolation
import matplotlib.pyplot as plt
import csv

def plot_data(csv_file: str) -> None:
    with open(csv_file, "r") as data:
        points = csv.reader(data)
        points: List[List[str]] = [[point[0], point[1]] for point in points]
        try:
            points = [[float(point[0]), float(point[1])] for point in points]
        except ValueError:
            points = [[float(point[0]), float(point[1])] for point in points[1:]]
        points = [Point.from_list(point) for point in points]

        x = [point.x for point in points]
        y = [point.y for point in points]

        plt.plot(x, y, label="pomiary")
        plt.xlabel(r"dystans $[m]$")
        plt.ylabel(r"wysokość $[m]$")
        plt.title(csv_file)
        plt.legend()
        plt.grid()
        plt.show()

def lagrange_data_plot(csv_file: str, split:int = 2) -> None:
    with open(csv_file, "r") as data:
        points = csv.reader(data)
        points: List[List[str]] = [[point[0], point[1]] for point in points]
        try:
            points = [[float(point[0]), float(point[1])] for point in points]
        except ValueError:
            points = [[float(point[0]), float(point[1])] for point in points[1:]]
        points = [Point.from_list(point) for point in points]

        x = [point.x for point in points]
        y = [point.y for point in points]

        mid_points: int  = split - 2
        step: int = len(points) - 1
        if mid_points != 0:
            step = (len(points) - 1) // (mid_points + 1)

        if step == 0:
            raise ValueError(f"Provided split is too big, max {len(points)}")

        split_points = x[0::step][:-1] + [x[-1]]

        f = lagrange_interpolation(points, split)

        plt.plot(x, y, label="pomiary")
        plt.plot([split_points[0] + i * 0.01 * (split_points[-1] - split_points[0]) for i in range(101)],\
                 [f(i) for i in [split_points[0] + i * 0.01 * (split_points[-1] - split_points[0]) for i in range(101)]],\
                 label="interpolacja Lagrange'a")
        plt.scatter(split_points, [f(i) for i in split_points], color="red", label="węzły interpolacji")
        plt.xlabel(r"dystans $[m]$")
        plt.ylabel(r"wysokość $[m]$")
        plt.title(csv_file)
        plt.legend()
        plt.grid()
        plt.show()

def cubic_spline_data_plot(csv_file: str, split:int = 2) -> None:
    with open(csv_file, "r") as data:
        points = csv.reader(data)
        points: List[List[str]] = [[point[0], point[1]] for point in points]
        try:
            points = [[float(point[0]), float(point[1])] for point in points]
        except ValueError:
            points = [[float(point[0]), float(point[1])] for point in points[1:]]
        points = [Point.from_list(point) for point in points]

        x = [point.x for point in points]
        y = [point.y for point in points]

        mid_points: int  = split - 2
        step: int = len(points) - 1
        if mid_points != 0:
            step = (len(points) - 1) // (mid_points + 1)

        if step == 0:
            raise ValueError(f"Provided split is too big, max {len(points)}")

        split_points = x[0::step][:-1] + [x[-1]]

        f = cubic_spline_interpolation(points, split)

        plt.plot(x, y, label="pomiary")
        plt.plot([split_points[0] + i * 0.001 * (split_points[-1] - split_points[0]) for i in range(1001)],\
                 [f(i) for i in [split_points[0] + i * 0.001 * (split_points[-1] - split_points[0]) for i in range(1001)]],\
                 label="interpolacja splajnami")
        plt.scatter(split_points, [f(i) for i in split_points], color="red", label="węzły interpolacji")
        plt.xlabel(r"dystans $[m]$")
        plt.ylabel(r"wysokość $[m]$")
        plt.title(csv_file)
        plt.legend()
        plt.grid()
        plt.show()
