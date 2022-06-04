from typing import Callable, List
from data_structures import Point

def lagrange_interpolation_function(points: List[Point]) -> Callable[[float], float]:
    def f(x: float) -> float:
        result = 0
        n = len(points)

        for point_i in points:
            base: float = 1.0
            for point_j in points:
                if point_i == point_j:
                    continue
                else:
                    base *= (x - point_j.x) / (point_i.x - point_j.x)
            result += point_i.y * base
        return result
    return f

def lagrange_interpolation(points: List[Point], split: int = 2):
    mid_points: int = split - 2
    step: int = len(points) - 1
    if mid_points != 0:
        step = (len(points) - 1) // (mid_points + 1)

    lagrange: Callable[[float], float] = lagrange_interpolation_function([point for point in points][0::step])

    return lagrange


