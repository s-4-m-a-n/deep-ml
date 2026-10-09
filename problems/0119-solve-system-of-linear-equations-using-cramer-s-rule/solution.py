import numpy as np

def cramers_rule(A, b):
    A = np.array(A)
    n_rows, n_cols = A.shape

    b = np.array(b)

    D = np.linalg.det(A)
    if D == 0:
        return -1

    x = np.zeros(n_cols)
    for c in range(n_cols):
        A_aug = A.copy()
        A_aug[:, c] = b 

        d = np.linalg.det(A_aug)
        x[c] = d/D

    return x