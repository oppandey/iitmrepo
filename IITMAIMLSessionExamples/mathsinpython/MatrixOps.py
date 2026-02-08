def matrix_addition(A, B):
    """Adds two matrices A and B."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must be of the same dimensions to add.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtraction(A, B):
    """Subtracts matrix B from matrix A."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must be of the same dimensions to subtract.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def matrix_multiplication(A, B):
    """Multiplies two matrices A and B."""
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to number of rows in B.")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose_matrix(A):
    """Transposes matrix A."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def determinant(A):
    """Calculates the determinant of matrix A (only for 2x2 and 3x3 matrices)."""
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to calculate determinant.")
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    elif len(A) == 3:
        return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
            A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
            A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
print(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # Example usage
print(matrix_subtraction([[5, 6], [7, 8]], [[1, 2], [3, 4]]))  # Example usage
print(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # Example usage
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  # Example usage
print(determinant([[1, 2], [3, 4]]))  # Example usage