from dataclasses import dataclass, field
from typing import List, Union
from vector import Vector
from operations import linear_combination
Number = Union[int, float]


@dataclass
class Matrix:
    """Matrix object stored as lines"""
    lines: List[List[Number]]
    columns: List[List[Number]] = field(init=False)
    m: int = field(init=False)
    n: int = field(init=False)

    @property
    def shape(self):
        return (self.m, self.n)

    @staticmethod
    def identity(n: int):
        """return identity matrix of range n"""
        mat = []
        for i in range(n):
            mat.append([0] * n)
        for i in range(n):
            for j in range(n):
                if j == i:
                    mat[i][j] = 1
        return Matrix(mat)

    def is_square(self):
        return self.m == self.n

    def __post_init__(self):
        # check that lines is a list
        if not isinstance(self.lines, list):
            raise TypeError("lines must be a list")
        # check that lines exists
        if len(self.lines) == 0:
            raise ValueError("lines cannot be empty")
        # m and n
        self.m = len(self.lines)
        self.n = len(self.lines[0])
        # check that lines contain real numbers + convert in float
        for li in self.lines:
            if not isinstance(li, list):
                raise TypeError("each line must a list")
            if len(li) != self.n:
                raise ValueError("each line must have length m")
            for i, v in enumerate(li):
                if not isinstance(v, (int, float)):
                    raise TypeError("matrix values must be real numbers")
                li[i] = float(v)
        # columns
        self.columns = []
        for k in range(self.n):
            col = [0] * self.m
            for i, li in zip(range(self.m), self.lines):
                col[i] = li[k]
            self.columns.append(col)

    def __str__(self):
        rows = []
        text = ""
        for i in range(self.m):
            row = [self.lines[i][j] for j in range(self.n)]
            rows.append(row)
            text = text + f"{row}\n"
        return text

    def __add__(self, other: "Matrix"):
        """add two Matrix of the same size"""
        if not isinstance(other, Matrix):
            raise TypeError("'other' must be a Matrix!")
        if self.shape != other.shape:
            raise ValueError("matrices must have the same shape!")
        result_lines = []
        for li_a, li_b in zip(self.lines, other.lines):
            result_lines.append([a + b for a, b in zip(li_a, li_b)])
        return Matrix(result_lines)

    def __sub__(self, other: "Matrix"):
        """subtract a Matrix by another Matrix"""
        if not isinstance(other, Matrix):
            raise TypeError("'other' must be a Matrix!")
        if self.shape != other.shape:
            raise ValueError("matrices must have the same shape!")
        result_lines = []
        for li_a, li_b in zip(self.lines, other.lines):
            result_lines.append([a - b for a, b in zip(li_a, li_b)])
        return Matrix(result_lines)

    def __mul__(self, scalar):
        """compute the scaling of a Matrix by a scalar"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("scalar must be a number")
        result_lines = []
        for li in self.lines:
            result_lines.append([float(scalar) * v for v in li])
        return Matrix(result_lines)

    def mul_vec(self, vec: Vector) -> Vector:
        if vec.size != self.n:
            raise ValueError("incorrect size of Vector!")
        vects = []
        for col in self.columns:
            vects.append(Vector(col))
        return linear_combination(vects, vec.values)

    def mul_mat(self, mat: "Matrix") -> "Matrix":
        if mat.m != self.n:
            raise ValueError("incorrect size of Matrix!")
        vects = []
        for li in mat.lines:
            vects.append(Vector(li))
        return Matrix([linear_combination(vects, self.lines[i]).values
                       for i in range(mat.m)])

    def trace(self) -> float:
        if not self.is_square():
            raise ValueError("matrix must be square!")
        return sum([self.lines[i][i] for i in range(self.m)])

    def transpose(self) -> "Matrix":
        transpose = []
        for j in range(self.n):
            transpose.append(self.columns[j])
        return Matrix(transpose)

    def row_echelon(self) -> "Matrix":
        """compute and return the row echelon form"""
        m = self.lines
        line = 0
        for j in range(self.n):
            # trouver le pivot et echanger les lignes
            for i in range(line, self.m):
                if m[i][j] and i != line:
                    m[line], m[i] = m[i], m[line]
                    break
            pivot = m[line][j]
            # si pivot nul, passer a la colonne suivante
            if pivot == 0:
                continue
            # mettre le pivot a 1
            m[line] = [x / pivot for x in m[line]]
            # mettre a zero le reste de la colonne
            for i in range(self.m):
                if i != line:
                    coef = m[i][j]
                    m[i] = [x - coef * y for x, y in zip(m[i], m[line])]
            line += 1
        return self

    def det_2(self) -> float:
        """determinant for matrix of dimension 2"""
        if not self.shape == (2, 2):
            raise ValueError("matrix must be a square of dimension 2!")
        m = self.lines
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    def det_3(self) -> float:
        """determinant for matrix of dimension 3"""
        if not self.shape == (3, 3):
            raise ValueError("matrix must be a square of dimension 3!")
        m = self.lines
        calc = []
        for i in range(self.m):
            coef = m[i][0]
            mat = [[m[(i + 1) % 3][1], m[(i + 1) % 3][2]],
                   [m[(i + 2) % 3][1], m[(i + 2) % 3][2]]]
            calc.append(coef * Matrix(mat).det_2())
        return sum(calc)

    def determinant(self) -> float:
        """compute and return the determinant"""
        if not self.is_square():
            raise ValueError("matrix must be square!")
        if self.m == 1:
            return self.lines[0][0]
        if self.shape == (2, 2):
            return self.det_2()
        if self.shape == (3, 3):
            return self.det_3()
        if self.m == 4:
            m = self.lines
            calc = []
            for i in range(self.m):
                coef = m[i][0] * (-1) ** i
                mat = [[m[(i + 1) % 4][1], m[(i + 1) % 4][2], m[(i + 1) % 4][3]
                        ],
                       [m[(i + 2) % 4][1], m[(i + 2) % 4][2], m[(i + 2) % 4][3]
                        ],
                       [m[(i + 3) % 4][1], m[(i + 3) % 4][2], m[(i + 3) % 4][3]
                        ]]
                calc.append(coef * Matrix(mat).det_3())
            return sum(calc)
        raise ValueError("matrix must be range 4 or smaller!")

    def inverse(self) -> "Matrix":
        """compute and return the inverse"""
        if not self.is_square():
            raise ValueError("matrix must be square!")
        if self.determinant() == 0:
            raise ValueError("matrix must not be singular!")
        id = Matrix.identity(self.m)
        augmented = []
        for i in range(self.m):
            augmented.append(self.lines[i] + id.lines[i])
        augmented = Matrix(augmented)
        augmented = augmented.row_echelon()
        inverse = id
        for i in range(self.m):
            for j in range(self.m, self.m * 2):
                inverse.lines[i][j - self.m] = augmented.lines[i][j]
        return inverse

    def rank(self) -> int:
        """return the rank of the matrix"""
        ref = self.row_echelon()

        def is_zero_row(row):
            return all(abs(x) < 1e-9 for x in row)

        rank = 0
        for i in range(ref.m):
            if not is_zero_row(ref.lines[i]):
                rank += 1
            else:
                return rank
        return rank
