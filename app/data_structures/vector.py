from typing import List

class vector:

    def __init__(self, vector: List[float]) -> None:
        self.vector = vector
        self.length = len(vector)

    def __len__(self) -> int:
        return self.length

    def __eq__(self, __o: object) -> bool:
        if type(__o) != type(self):
            return False

        for i in range(len(self)):
            if __o.vector[i] != self.vector[i]:
                return False

        return True

    def __add__(self, __o: "vector") -> "vector":
        if len(self) != len(__o):
            raise Exception("Vectors have to be of equal lengths in order to add them!")
        return vector([i + j for i, j in zip(self.vector, __o.vector)])

    def __sub__(self, __o: "vector") -> "vector":
        if len(self) != len(__o):
            raise Exception("Vectors have to be of equal lengths in order to subtract them!")
        return vector([i - j for i, j in zip(self.vector, __o.vector)])

    def __getitem__(self, key: int) -> float:
        return self.vector[key]

    def __setitem__(self, key: int, item: float) -> None:
        self.vector[key] = item

    def __str__(self) -> str:
        str_representation: str = ""
        for element in self.vector:
            str_representation += f"|{element:10.4e}|\n"

        return str_representation

    @property
    def norm(self) -> float:
        return sum([element ** 2 for element in self.vector]) ** 0.5

    @property
    def vector(self) -> List[float]:
        return self._vector

    @vector.setter
    def vector(self, vector: List[float]) -> None:
        self._vector = vector
        self.length = len(vector)

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self._length = length

    def copy(self) -> "vector":
        copy_list = [element for element in self.vector]
        return vector(copy_list)

    @staticmethod
    def zeros(n: int) -> "vector":
        return vector([0.0 for _ in range(n)])

    @staticmethod
    def ones(n: int) -> "vector":
        return vector([1.0 for _ in range(n)])
