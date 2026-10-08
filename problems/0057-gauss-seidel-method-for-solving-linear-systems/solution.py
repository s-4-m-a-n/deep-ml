import numpy as np

def gauss_seidel(A, b, n=100, x_ini=None):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n_rows, n_cols = A.shape
    
    x = np.zeros(n_rows) if x_ini is None else np.array(x_ini, dtype=float)

    for _ in range(n):
        for i in range(n_rows):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]

    return x