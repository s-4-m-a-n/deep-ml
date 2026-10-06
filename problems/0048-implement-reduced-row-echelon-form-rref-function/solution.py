import numpy as np

def rref(matrix, tol=1e-10):
    A = np.array(matrix, dtype=np.float64)

    n_rows, n_cols = A.shape
    pivot_row = 0

    for c in range(n_cols):

        if pivot_row >= n_rows:
            break

        # Find largest absolute value in this column
        max_offset_row = np.argmax(
            np.abs(A[pivot_row:, c])
        )
        max_row_idx = pivot_row + max_offset_row

        # No valid pivot
        if np.abs(A[max_row_idx, c]) < 1e-10:
            continue

        # Swap pivot row
        A[[pivot_row, max_row_idx]] = \
            A[[max_row_idx, pivot_row]]

        # Normalize pivot to 1
        A[pivot_row] /= A[pivot_row, c]

        # Eliminate ABOVE and BELOW pivot
        for r in range(n_rows):

            if r == pivot_row:
                continue

            factor = A[r, c]

            A[r] -= factor * A[pivot_row]

        pivot_row += 1

    # Remove floating-point noise
    A[np.abs(A) < tol] = 0

    return A