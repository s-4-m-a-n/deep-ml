import numpy as np

def rref(matrix):
    matrix = np.array(matrix, dtype=float)

    m, n = matrix.shape
    pivot_row = 0

    for pivot_col in range(n):

        # Find a non-zero pivot
        pivot = None

        for r in range(pivot_row, m):
            if matrix[r, pivot_col] != 0:
                pivot = r
                break

        if pivot is None:
            continue

        # Swap rows
        matrix[[pivot_row, pivot]] = matrix[[pivot, pivot_row]]

        # Normalize pivot row
        matrix[pivot_row] /= matrix[pivot_row, pivot_col]

        # Eliminate pivot column from all other rows
        for r in range(m):
            if r == pivot_row:
                continue

            matrix[r] -= matrix[r, pivot_col] * matrix[pivot_row]

        pivot_row += 1

        if pivot_row == m:
            break

    return matrix