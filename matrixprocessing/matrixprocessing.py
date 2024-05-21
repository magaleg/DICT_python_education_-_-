"""Project Matrix processing"""


def read_matrix():
    """
    Reads inputted matrix.

    :returns: tuple: (n, m) dimensions and the matrix itself
    """
    n, m = map(int, input("Enter size of matrix: ").split())
    matrix = []
    print("Enter matrix:")
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return n, m, matrix


def read_constant():
    """
    Reads a constant value from the user input.

    Reads the inputted constant.
    :returns:
    float: inputted constant
    """
    return float(input("Enter constant: "))


def add_matrices(matrix_a, matrix_b):
    """
    Adds two matrices together element-wise.

    :param matrix_a: tuple of dimensions and elements of the 1 matrix to add
    :param matrix_b: tuple of dimensions and elements of the 2 matrix to add
    :returns:
    list of str: returns the result or ERROR if something went wrong
    """
    n_a, m_a, a = matrix_a
    n_b, m_b, b = matrix_b

    if n_a != n_b or m_a != m_b:
        return "ERROR"

    result = []
    for i in range(n_a):
        row = []
        for j in range(m_a):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def multiply_matrix_by_constant(matrix, constant):
    """
     Multiplies a matrix by a constant scalar.

    :param: matrix (tuple):The matrix represented as a tuple containing its dimensions and elements.
    :param: constant (float): The constant scalar to multiply the matrix by.
    :returns:
    list: The resulting matrix after multiplication by the constant.
    """
    n, m, mat = matrix
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(mat[i][j] * constant)
        result.append(row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    """
     Multiplies two matrices together.

    :param: matrix_a (tuple): The first matrix represented as a tuple containing its dimensions and elements.
    :param: matrix_b (tuple): The second matrix represented as a tuple containing its dimensions and elements.
    :returns: list or str: The resulting matrix if multiplication is possible, otherwise returns "ERROR".
    """
    n_a, m_a, a = matrix_a
    n_b, m_b, b = matrix_b

    if m_a != n_b:
        return "ERROR"

    result = [[0] * m_b for _ in range(n_a)]
    for i in range(n_a):
        for j in range(m_b):
            for k in range(m_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transpose_main_diagonal(matrix):
    """
    Transposes a matrix along its main diagonal.

    :param: (tuple): The matrix represented as a tuple containing its dimensions and elements.
    :returns: (list) the transposed matrix along its main diagonal.
    """
    n, m, mat = matrix
    result = [[mat[j][i] for j in range(n)] for i in range(m)]
    return result


def transpose_side_diagonal(matrix):
    """
    Transposes a matrix along its side diagonal.

    :param: matrix (tuple): The matrix represented as a tuple containing its dimensions and elements.
    :returns: (list) The transposed matrix along its side diagonal.
    """
    n, m, mat = matrix
    result = [[mat[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]
    return result


def transpose_vertical_line(matrix):
    """
    Transposes a matrix along a vertical line.

    :param matrix: (tuple), the matrix represented as a tuple containing its dimensions and elements.
    :returns: (list) The transposed matrix along a vertical line.
    """
    n, m, mat = matrix
    result = [[mat[i][m - 1 - j] for j in range(m)] for i in range(n)]
    return result


def transpose_horizontal_line(matrix):
    """
    Transposes a matrix along a horizontal line.

    :param matrix: (tuple), the matrix represented as a tuple containing its dimensions and elements.
    :returns: (list) The transposed matrix along a horizontal line.
    """
    n, m, mat = matrix
    result = [[mat[n - 1 - i][j] for j in range(m)] for i in range(n)]
    return result


def determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    :param matrix: (tuple) the matrix represented as a tuple containing its dimensions and elements.
    :returns: returns the result or ERROR if something went wrong
    """
    n, m, mat = matrix

    if n != m:
        return "ERROR"

    if n == 1:
        return mat[0][0]

    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    det = 0
    for c in range(m):
        det += ((-1) ** c) * mat[0][c] * determinant((n - 1, m - 1, [row[:c] + row[c + 1:] for row in mat[1:]]))
    return det


def inverse_matrix(matrix):
    """
    Calculates the inverse of a square matrix.

    :param matrix: (tuple) The matrix represented as a tuple containing its dimensions and elements.
    :returns: (list or str): The inverse matrix if calculation is possible, otherwise returns error
    """
    n, m, mat = matrix

    if n != m:
        return "ERROR"

    det = determinant(matrix)
    if det == 0:
        return "This matrix doesn't have an inverse."

    if n == 1:
        return [[1 / mat[0][0]]]

    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(m):
            minor = [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]
            cofactor_row.append(((-1) ** (i + j)) * determinant((n - 1, m - 1, minor)))
        cofactors.append(cofactor_row)

    adjugate = transpose_main_diagonal((n, m, cofactors))
    inverse = multiply_matrix_by_constant((n, m, adjugate), 1 / det)
    return inverse


def print_matrix(matrix):
    """
    Prints the matrix.

    :param matrix: either matrix (tuple) or ERROR (str)
    :returns: none
    """
    if matrix == "ERROR":
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        for row in matrix:
            print(" ".join(map(str, row)))


def main():
    """
    The main program function. Runs loop allowing user to choose between operations,
    then runs chosen one.

    :returns: none
    """
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ")

        if choice == '0':
            break
        elif choice == '1':
            print("Enter size of first matrix: ", end='')
            matrix_a = read_matrix()
            print("Enter size of second matrix: ", end='')
            matrix_b = read_matrix()
            result = add_matrices(matrix_a, matrix_b)
            print_matrix(result)
        elif choice == '2':
            print("Enter size of matrix: ", end='')
            matrix = read_matrix()
            constant = read_constant()
            result = multiply_matrix_by_constant(matrix, constant)
            print_matrix(result)
        elif choice == '3':
            print("Enter size of first matrix: ", end='')
            matrix_a = read_matrix()
            print("Enter size of second matrix: ", end='')
            matrix_b = read_matrix()
            result = multiply_matrices(matrix_a, matrix_b)
            print_matrix(result)
        elif choice == '4':
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            transpose_choice = input("Your choice: > ")
            print("Enter matrix size: ", end='')
            matrix = read_matrix()
            if transpose_choice == '1':
                result = transpose_main_diagonal(matrix)
            elif transpose_choice == '2':
                result = transpose_side_diagonal(matrix)
            elif transpose_choice == '3':
                result = transpose_vertical_line(matrix)
            elif transpose_choice == '4':
                result = transpose_horizontal_line(matrix)
            else:
                print("Invalid choice, please try again.")
                continue
            print_matrix(result)
        elif choice == '5':
            print("Enter matrix size: ", end='')
            matrix = read_matrix()
            det = determinant(matrix)
            if det == "ERROR":
                print("The operation cannot be performed.")
            else:
                print("The result is:")
                print(det)
        elif choice == '6':
            print("Enter matrix size: ", end='')
            matrix = read_matrix()
            inverse = inverse_matrix(matrix)
            print_matrix(inverse)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

