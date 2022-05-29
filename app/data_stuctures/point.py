from typing import List


class Point:

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    @classmethod
    def from_list(cls, coords: List[float]) -> "Point":
        return cls(coords[0], coords[1])

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float) -> None:
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = y

