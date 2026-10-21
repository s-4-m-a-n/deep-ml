import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """
    Perform QR decomposition using the Modified Gram-Schmidt process.
    
    Args:
        A: An m x n matrix represented as list of lists
    
    Returns:
        Tuple of (Q, R) where Q is orthogonal and R is upper triangular
    """
    A_arr = np.array(A, dtype=float)
    m, n = A_arr.shape
    
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    # Copy A to track the orthogonalizing vectors
    V = A_arr.copy()
    
    for i in range(n):
        # Compute the norm of the current column
        norm_v = np.linalg.norm(V[:, i])
        R[i, i] = norm_v
        
        if norm_v == 0:
            Q[:, i] = 0
        else:
            Q[:, i] = V[:, i] / norm_v
            
        # Orthogonalize the remaining columns against the current column
        for j in range(i + 1, n):
            R[i, j] = np.dot(Q[:, i], V[:, j])
            V[:, j] = V[:, j] - R[i, j] * Q[:, i]
            
    return Q.tolist(), R.tolist()