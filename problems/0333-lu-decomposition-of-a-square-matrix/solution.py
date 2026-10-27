import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    
    Args:
        A: Square matrix as a list of lists
    
    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    A = np.array(A)
    n = A.shape[0]

    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n): # for each col of U
        for k in range(i, n): #upper trangle
            s1 = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s1
        
        for k in range(i+1, n): # for each row of L
            s1 = sum(L[k][j] * U[j][i] for j in range(i))
            if U[i][i] == 0:
                raise ValueError("Division by zero: Pivot is zero. LU decomposition without pivoting fails.")
            L[k][i] = (A[k][i] - s1) / U[i][i]

    return L, U