from dataclasses import dataclass
from math import sqrt


@dataclass
class Vector:
    """Vector object"""
    values: list

    def __post_init__(self):
        # check that values is a list
        if not isinstance(self.values, list):
            raise TypeError("values must be a list")
        # check that values exists
        if len(self.values) == 0:
            raise ValueError("values cannot be empty")
        # check that values contain real numbers + convert in float
        for i, v in enumerate(self.values):
            if not isinstance(v, (int, float)):
                raise TypeError("values must contain only real numbers")
            self.values[i] = float(v)

    @property
    def size(self):
        """return the size of the Vector"""
        return len(self.values)

    def __str__(self):
        text = ""
        for i in range(self.size):
            x = self.values[i]
            text = text + f"[{x}]\n"
        return text

    def __add__(self, other: "Vector"):
        """add two vectors of the same size"""
        if not isinstance(other, Vector):
            raise TypeError("'other' must be a Vector!")
        if self.size != other.size:
            raise ValueError("Vectors must be the same size!")
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __sub__(self, other: "Vector"):
        """subtract a vector by another vector"""
        if not isinstance(other, Vector):
            raise TypeError("'other' must be a Vector!")
        if self.size != other.size:
            raise ValueError("Vectors must be the same size!")
        result = [a - b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, scalar):
        """compute the scaling of a vector by a scalar"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("scalar must be a number")
        result = [float(scalar) * v for v in self.values]
        return Vector(result)

    def dot(self, other: "Vector"):
        """compute dot product of two vectors of the same size"""
        if not isinstance(other, Vector):
            raise TypeError("'other' must be a Vector!")
        if self.size != other.size:
            raise ValueError("Vectors must be the same size!")
        result = 0
        for i, j in zip(self.values, other.values):
            result += i * j
        return result

    def norm_1(self):
        """Manhattan norm: sum of the Vector's absolute values"""
        return sum([abs(x) for x in self.values])

    def norm(self):
        """Euclidean norm:
        square root of the sum of the Vector's squared values"""
        # return pow(sum([pow(x, 2) for x in self.values]), 1/2)
        return sqrt(sum([abs(x) ** 2 for x in self.values]))

    def norm_inf(self):
        """Supremum norm: max(|v(i)|)"""
        return max([abs(x) for x in self.values])
