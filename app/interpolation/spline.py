from typing import Callable, List, Union
from data_structures import matrix
from data_structures import vector
from data_structures import Point

def cubic_spline_interpolation(points: List[Point], split: int = 2) -> Callable[[float], float]:

    mid_points: int = split - 2
    step: int = len(points) - 1
    if mid_points != 0:
        step = (len(points) - 1) // (mid_points + 1)

    interpolation_points: List[Point] = [point for point in points][0::step]

    def get_params() -> vector:
        n: int  = len(points)
        # n points, gives n-1 intervals, which gives 4(n-1) equations
        # matrix A is of size (4(n-1)) x (4(n-1)) and (4(n-1)) elements inside of vectors x and b
        # x = [a_0, b_0, c_0, d_0, ..., a_{n-1}, b_{n-1}, c_{n-1}, d_{n-1}]3

        A = matrix.zeros(4*(n-1))
        b = vector.zeros(4*(n-1))

        # 1. S_i(x_i) = f(x_i)
        for i in range(n-1):
            _, y = points[i].tuple
            row: List[float] = [0.0 for _ in range(4*(n-1))]
            row[4*i + 3] = 1
            A.matrix[4*i + 3] = row
            b[4*i + 3] = y

        # 2. S_i(x_{i+1}) = f(x_{i+1})
        for i in range(n-1):
            x_0, _ = points[i].tuple
            x_1, y_1 = points[i+1].tuple
            h: float = x_1 - x_0
            row: List[float] = [0.0 for _ in range(4*(n-1))]
            row[4*i] = h ** 3
            row[4*i + 1] = h ** 2
            row[4*i + 2] = h
            row[4*i + 3] = 1
            A.matrix[4*i + 2] = row
            b[4*i + 2] = y_1

        # 3. S_{i-1}'(x_i) = S_i'(x_i)
        for i in range(n-2):
            x_0, _ = points[i].tuple
            x_1, y_1 = points[i+1].tuple
            h: float = x_1 - x_0
            row: List[float] = [0.0 for _ in range(4*(n-1))]
            row[4*i] = 3 * h**2
            row[4*i + 1] = 2 * h
            row[4*i + 2] = 1
            row[4*(i + 1) + 2] = -1
            A.matrix[4*i] = row
            b[4*i] = 0.0

        # 4. S_{i-1}''(x_i) = S_{i}''(x_i)
        for i in range(n-2):
            x_0, _ = points[i].tuple
            x_1, y_1 = points[i+1].tuple
            h: float = x_1 - x_0
            row: List[float] = [0.0 for _ in range(4*(n-1))]
            row[4*i] = 6*h
            row[4*i + 1] = 2
            row[4*(i+1) + 1] = -2
            A.matrix[4*(i+1) + 1] = row
            b[4*(i+1) + 1] = 0.0

        row: List[float] = [0.0 for _ in range(4*(n-1))]
        row[1] = 2
        A.matrix[1] = row
        b[1] = 0.0

        row: List[float] = [0.0 for _ in range(4*(n-1))]
        x_0, y_0 = points[-2].tuple
        x_1, y_1 = points[-1].tuple
        h: float = x_1 - x_0
        row[1] = 2
        row[-4] = 6 * h
        A.matrix[-4] = row
        b[-4] = 0.0

        _, params, _ = A.lu_factorization(b)
        return params

    params: vector = get_params()

    def f(x: float) -> Union[float, None]:
        p_list = []
        row = []
        for param in params.vector:
            p_list.append(param)
            if len(row) == 4:
                p_list.append(row)
                row.clear()

        for i in range(1, len(points)):
            x_i, y_i = points[i-1].tuple
            x_j, y_j = points[i].tuple
            if x_i <= x <= x_j:
                a, b, c, d = p_list[i-1]
                h = x - x_i
                return a*(h**3) + b*(h**2) + c*h + d

        return None

    return f

