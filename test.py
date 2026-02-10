from vector import Vector
from matrix import Matrix
from operations import angle_cos, cross_product
from operations import linear_combination, linear_interpolation


def ex00():
    print("\nEX00: add, substract and scale\n")
    print("\nVECTOR\n")
    try:

        v1 = Vector([2, 3])
        v2 = Vector([5, 7])
        v3 = v1 + v2
        v4 = v1 - v2
        print(v3)
        print(v4)
        print(v1 * 2)

    except Exception as e:
        print(e)

    print("\n")

    try:
        v1 = Vector([1, 2, 3])
        v2 = Vector([10.0, 20.0, 30.0])
        v3 = Vector([3])

        print(v1)
        print(v2)

        v3 = v1 + v2
        v4 = v1 - v2
        v5 = v1 * 2

        print(v3)  # [11.0, 22.0, 33.0]
        print(v4)  # [-9.0, -18.0, -27.0]
        print(v5)  # [2.0, 4.0, 6.0]
    except Exception as e:
        print(e)

    print("\nMATRIX\n")

    try:
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[7, 4], [-2, 2]])
        print(A + B)
        print(A - B)
        print(A * 2)

        print("\n")

        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[10, 20], [30, 40]])

        print("Matrix A:")
        print(A)
        print("Matrix B:")
        print(B)
        print(A.shape)
        print(A.is_square())

        print("\nADD:")
        print(A + B)
        print("\nSUB:")
        print(B - A)
        print("\nSCL:")
        print(A * 2)
    except Exception as e:
        print(e)


def ex01():
    print("\nEX01: linear combination\n")
    try:
        e1 = Vector([1, 0, 0])
        e2 = Vector([0, 1, 0])
        e3 = Vector([0, 0, 1])

        v1 = Vector([1, 2, 3])
        v2 = Vector([0, 10, -100])

        print(linear_combination([e1, e2, e3], [10, -2, 0.5]))
        print(linear_combination([v1, v2], [10, -2]))

    except Exception as e:
        print(e)

    # Errors
    print("\nERRORS:\n")
    try:
        print(linear_combination([v1], [10, -2]))
    except Exception as e:
        print("Error:", e)

    try:
        print(linear_combination([10, -2], [10, -2]))
    except Exception as e:
        print("Error:", e)


def ex02():
    try:
        print("\nEX02: linear interpolation\n")

        print(linear_interpolation(0, 1, 0))
        print(linear_interpolation(0, 1, 1))
        print(linear_interpolation(0, 1, 0.5))
        print(linear_interpolation(21, 42, 0.3))

        print("\nVECTOR\n")
        print(linear_interpolation(Vector([2., 1.]),
                                   Vector([4., 2.]),
                                   0.3))
        print("\nMATRIX\n")
        print(linear_interpolation(Matrix([[2., 1.], [3., 4.]]),
                                   Matrix([[20., 10.], [30., 40.]]),
                                   0.5))
        print("\nERROR\n")
        print(linear_interpolation(Matrix([[2., 1.], [3., 4.]]),
                                   Vector([20., 10.]),
                                   0.5))

    except Exception as e:
        print("Error:", e)


def ex03():
    try:
        print("\nEX03: dot product\n")
        v1 = Vector([0, 0])
        v2 = Vector([1, 1])
        print(v1.dot(v2))

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        print(v1.dot(v2))

        v1 = Vector([-1., 6.])
        v2 = Vector([3., 2.])
        print(v1.dot(v2))

        print("\nERROR\n")
        v1 = Vector([-1., 6.])
        v2 = Vector([3])
        print(v1.dot(v2))

    except Exception as e:
        print("Error:", e)


def ex04():
    try:
        print("\nEX04: norm\n")
        v1 = Vector([0., 0., 0.])
        print(v1.norm_1(), v1.norm(), v1.norm_inf())

        v1 = Vector([1., 2., 3.])
        print(v1.norm_1(), f"{v1.norm():0.9f}", v1.norm_inf())

        v1 = Vector([-1., -2.])
        print(v1.norm_1(), f"{v1.norm():0.9f}", v1.norm_inf())

    except Exception as e:
        print("Error:", e)


def ex05():
    try:
        print("\nEX05: cosine\n")
        v1 = Vector([1., 0.])
        v2 = Vector([1., 0.])
        print(angle_cos(v1, v2))

        v1 = Vector([1., 0.])
        v2 = Vector([0., 1.])
        print(angle_cos(v1, v2))

        v1 = Vector([-1., 1.])
        v2 = Vector([1., -1.])
        print(angle_cos(v1, v2))

        v1 = Vector([2., 1.])
        v2 = Vector([4., 2.])
        print(angle_cos(v1, v2))

        v1 = Vector([1., 2., 3.])
        v2 = Vector([4., 5., 6.])
        print(angle_cos(v1, v2))

        print("\nERROR\n")
        v1 = Vector([0, 0, 0])
        v2 = Vector([4., 5., 6.])
        print(angle_cos(v1, v2))

    except Exception as e:
        print("Error:", e)


def ex06():
    print("\nEX06: cross_product\n")
    try:
        v1 = Vector([0., 0., 1.])
        v2 = Vector([1., 0., 0.])
        print(cross_product(v1, v2))

        v1 = Vector([1., 2., 3.])
        v2 = Vector([4., 5., 6.])
        print(cross_product(v1, v2))

        v1 = Vector([4., 2., -3.])
        v2 = Vector([-2., -5., 16.])
        print(cross_product(v1, v2))

        print("\nERROR\n")
        v1 = Vector([0, 0, 0])
        v2 = Vector([4., 5., 6., 0])
        print(cross_product(v1, v2))

    except Exception as e:
        print("Error:", e)


def ex07():
    print("\nEX07: matrix multiplication\n")
    try:
        print("\nmul_vec:\n")
        A = Matrix([[1., 0.], [0., 1.]])
        v = Vector([4., 2.])
        print(A.mul_vec(v))

        A = Matrix([[2, 0.], [0., 2]])
        v = Vector([4., 2.])
        print(A.mul_vec(v))

        A = Matrix([[2., -2.], [-2., 2.]])
        v = Vector([4., 2.])
        print(A.mul_vec(v))

        print("\nmul_mat:\n")
        A = Matrix([[1., 0.], [0., 1.]])
        B = Matrix([[1., 0.], [0., 1.]])
        print(A.mul_mat(B))

        A = Matrix([[1., 0.], [0., 1.]])
        B = Matrix([[2, 1], [4, 2]])
        print(A.mul_mat(B))

        A = Matrix([[3., -5.], [6., 8.]])
        B = Matrix([[2, 1], [4, 2]])
        print(A.mul_mat(B))

        print("\nERROR\n")
        A = Matrix([[3., -5., 5], [6., 8., 5]])
        B = Matrix([[2, 1], [4, 2]])
        print(A.mul_mat(B))

    except Exception as e:
        print("Error:", e)


def ex08():
    print("\nEX08: trace\n")
    try:
        A = Matrix([[1., 0.], [0., 1.]])
        print(A.trace())

        A = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
        print(A.trace())

        A = Matrix([[-2., -8., 4.],
                    [1., -23., 4.],
                    [0., 6., 4.]])
        print(A.trace())

        print("\nERROR\n")
        A = Matrix([[-2., -8., 4., 1],
                    [1., -23., 4., 1],
                    [0., 6., 4., 1]])
        print(A.trace())

    except Exception as e:
        print("Error:", e)


def ex09():
    print("\nEX09: transpose\n")
    try:
        A = Matrix([[1., 0.], [0., 1.]])
        print("A:")
        print(A, "")
        print(A.transpose())

        A = Matrix([[2., -5., 0.],
                    [4., 3., 7.]])
        print("B:")
        print(A, "")
        print(A.transpose())

        A = Matrix([[-2., -8., 4.],
                    [1., -23., 4.],
                    [5., 5., 5.],
                    [0., 6., 4.]])
        print("C:")
        print(A, "")
        print(A.transpose())

        A = Matrix([[-2., -8., 4., 1],
                    [1., -23., 4., 1],
                    [0., 6., 4., 1]])
        print("D:")
        print(A, "")
        print(A.transpose())

    except Exception as e:
        print("Error:", e)


def ex10():
    print("\nEX10: row-echelon form\n")
    try:
        A = Matrix([[1., 0., 0.],
                    [0., 1., 0.],
                    [0., 0., 1.]])
        print("A:")
        print(A, "")
        print(A.row_echelon())

        A = Matrix([[1, 2],
                    [3, 4]])
        print("B:")
        print(A, "")
        print(A.row_echelon())

        A = Matrix([[1, 2],
                    [2, 4]])
        print("C:")
        print(A, "")
        print(A.row_echelon())

        A = Matrix([[8., 5., -2., 4., 28.],
                    [4., 2.5, 20., 4., -4.],
                    [8., 5., 1., 4., 17.]])
        print("D:")
        print(A, "")
        print(A.row_echelon())

        A = Matrix([[2, -1, 0],
                    [-1, 2, -1],
                    [0, -1, 2]])
        print("E:")
        print(A, "")
        print(A.row_echelon())

    except Exception as e:
        print("Error:", e)


def ex11():
    print("\nEX11: determinant\n")
    try:
        A = Matrix([[1., -1],
                    [-1, 1.]])
        print("A:")
        print(A, A.determinant(), "\n")
        A = Matrix([[2., 0., 0.],
                    [0., 2., 0.],
                    [0., 0., 2.]])
        print("B:")
        print(A, A.determinant(), "\n")
        A = Matrix([[8, 5, -2],
                    [4, 7, 20],
                    [7, 6, 1]])
        print("C:")
        print(A, A.determinant(), "\n")
        A = Matrix([[8., 5., -2., 4.],
                    [4., 2.5, 20., 4.],
                    [8., 5., 1., 4.],
                    [28., -4., 17., 1.]])
        print("D:")
        print(A, A.determinant(), "\n")
        A = Matrix([[2, -1, 0],
                    [-1, 2, -1],
                    [0, -1, 2]])
        print("E:")
        print(A, A.determinant(), "\n")

        A = Matrix([[1, 2],
                    [3, 4]])
        print("F:")
        print(A, A.determinant(), "\n")
        A = Matrix([[8., 5., -2., 4., 28.],
                    [4., 2.5, 20., 4., -4.],
                    [8., 5., 1., 4., 17.]])
        print("G:")
        print(A, "")
        print(A.determinant())

    except Exception as e:
        print("Error:", e)


def ex12():
    print("\nEX12: inverse\n")
    try:
        A = Matrix([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
        print("A:")
        print(A)
        print(A.inverse(), "\n")

        A = Matrix([[2, 0, 0],
                    [0, 2, 0],
                    [0, 0, 2]])
        print("B:")
        print(A)
        print(A.inverse(), "\n")

        A = Matrix([[8, 5, -2],
                    [4, 7, 20],
                    [7, 6, 1]])
        print("C:")
        print(A)
        print(A.inverse(), "\n")

    except Exception as e:
        print("Error:", e)


def ex13():
    print("\nEX13: RANK\n")
    try:
        A = Matrix([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])
        print("A:")
        print(A)
        print(A.rank(), "\n")

        A = Matrix([[1., 2., 0., 0.],
                    [2., 4., 0., 0.],
                    [-1., 2., 1., 1.]])
        print("B:")
        print(A)
        print(A.rank(), "\n")

        A = Matrix([[8, 5, -2],
                    [4, 7, 20],
                    [7, 6, 1],
                    [21., 18., 7.]])
        print("C:")
        print(A)
        print(A.rank(), "\n")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    ex00()
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()
    ex07()
    ex08()
    ex09()
    ex10()
    ex11()
    ex12()
    ex13()
