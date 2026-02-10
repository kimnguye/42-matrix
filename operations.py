from vector import Vector
from typing import List, Union
Number = Union[int, float]


def linear_combination(vects: List[Vector], lambdas: List[Number]) -> Vector:

    # checks
    if len(vects) != len(lambdas):
        raise ValueError("linear_combination:"
                         " the 2 arguments must have the same size!")

    if len(vects) == 0:
        raise ValueError("linear_combination: the list of vectors is empty!")

    for v, k in zip(vects, lambdas):
        if not isinstance(v, Vector):
            raise TypeError(
                "linear_combination:"
                " the first argument must be a list of Vectors")
        if not isinstance(k, Number):
            raise TypeError("linear_combination:"
                  " the 2nd argument must be a list of numbers")

    # calculation
    try:
        siz = vects[0].size
        lin_comb = Vector([0] * siz)
        for v, k in zip(vects, lambdas):
            lin_comb += v * k

    except Exception as e:
        print("Error catched:", e)
        return None

    return lin_comb


def linear_interpolation(u, v, t: float) -> Vector:
    if isinstance(u, type(v)):
        return u + (v - u) * t
    raise TypeError("linear_interpolation: u and v must be of the same type")


def angle_cos(u: Vector, v: Vector) -> float:
    if u.size != v.size:
        raise ValueError("Vectors must be the same size!")
    return round(u.dot(v) / (u.norm() * v.norm()), 9)


def cross_product(u: Vector, v: Vector) -> Vector:
    """only for 3-dimensional vectors"""
    if not (u.size == 3 and v.size == 3):
        raise ValueError("vectors must be 3-dimensional")
    result = [0, 0, 0]
    for i in range(3):
        j = (i + 1) % 3
        k = (i + 2) % 3
        result[i] = u.values[j] * v.values[k] - u.values[k] * v.values[j]
    return Vector(result)
