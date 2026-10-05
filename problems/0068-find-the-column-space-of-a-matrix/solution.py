import numpy as np

def matrix_image(A):
    A = np.array(A, dtype=np.float64)
    org_A = A.copy()
    
    n_rows, n_cols = A.shape
    pivot_row = 0
    rank = 0
    pivot_cols = []
    for c in range(n_cols):
        if pivot_row >= n_rows: #for non-square matrix
            break
            
        # Find row with the maximum absolute entry in column `c` from `pivot_row` down
        max_offset_row = np.argmax(np.abs(A[pivot_row:, c]))
        max_row_idx = pivot_row + max_offset_row

        # check tolerance
        if np.abs(A[max_row_idx, c]) < 1e-7:
            continue
        
        # and swap max row with the pivot row
        A[[pivot_row, max_row_idx]] = A[[max_row_idx, pivot_row]]

        # eliminate entries below the pivot
        for r in range(pivot_row+1, n_rows):
            factor = A[r, c] / A[pivot_row, c]
            A[r] = A[r] - factor * A[pivot_row]
        
        rank += 1
        pivot_row += 1
        pivot_cols.append(c)
    return org_A[:, pivot_cols]