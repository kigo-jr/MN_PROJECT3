from typing import Callable, List
from data_structures import matrix
from data_structures import vector
from data_structures import Point

def cubic_spline_interpolation_function(points: List[Point]) -> Callable[[float], float]:
    n: int = len(points)
    x_list: List[float] = [point.x for point in points]
    y_list: List[float] = [point.y for point in points]
    h_list: List[float] = [x_list[i+1] - x_list[i] for i in range(n - 1)] # dolna / górna przekątna
    mi_list: List[float] = [2*(h_list[i] + h_list[i+1]) for i in range(n - 2)] # główna przekątna
    b_list: List[float] = [(y_list[i+1] - y_list[i]) * 6 / h_list[i] for i in range(n - 1)]
    v_list: List[float] = [b_list[i+1] - b_list[i] for i in range(n-2)] # wektor wyrazów wolnych
    h_list = h_list[1:-1]
    v: vector = vector(v_list)
    A: matrix = matrix([
        [mi_list[i] if i==j else h_list[j] if j == i-1 else h_list[j-1] if j == i+1 else 0.0 for i in range(n-2)] for j in range(n-2)
    ])

    _, parameters, _ = A.lu_factorization(v)
    z_list: List[float] = [0.0]
    z_list.extend(parameters.vector)
    z_list.append(0.0)

    h_list: List[float] = [x_list[i+1] - x_list[i] for i in range(n - 1)]


    def interpolation(x: float) -> float:
        i: int = 0
        for index in range(n - 1):
            if x_list[index] <= x <= x_list[index+1]:
                i = index
                break

        value = z_list[i] / (6*h_list[i]) * (x_list[i+1] - x)**3 + z_list[i+1]/(6*h_list[i]) * (x-x_list[i]) ** 3\
              + (y_list[i+1] / h_list[i] - z_list[i+1] * h_list[i] / 6) * (x - x_list[i]) + (y_list[i] / h_list[i] - z_list[i] * h_list[i] / 6) * (x_list[i+1] - x)
        return value

    return interpolation

def cubic_spline_interpolation(points: List[Point], split: int = 2):
    mid_points: int = split - 2
    step: int = len(points) - 1
    if mid_points != 0:
        step = (len(points) - 1) // (mid_points + 1)

    interpolation: Callable[[float], float] = cubic_spline_interpolation_function([point for point in points][0::step])
    return interpolation


