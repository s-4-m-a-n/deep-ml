import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]] | int:
    """
    Transforms matrix A using the operation T^(-1) * A * S.
    Validates that T and S are invertible and dimensions are compatible.
    Returns the resulting matrix as a list of lists, or -1 if invalid.
    """
    try:
        # Convert inputs to NumPy arrays
        A_arr = np.array(A, dtype=float)
        T_arr = np.array(T, dtype=float)
        S_arr = np.array(S, dtype=float)
        
        # Ensure all inputs are 2D matrices
        if A_arr.ndim != 2 or T_arr.ndim != 2 or S_arr.ndim != 2:
            return -1
            
        m, n = A_arr.shape
        
        # T must be m x m and S must be n x n for the operation to be valid
        if T_arr.shape != (m, m) or S_arr.shape != (n, n):
            return -1
            
        # Validate invertibility by attempting to compute inverses.
        # np.linalg.inv raises LinAlgError if a matrix is singular (not invertible).
        T_inv = np.linalg.inv(T_arr)
        _ = np.linalg.inv(S_arr)  # Validates that S is invertible
        
        # Perform the transformation: T^(-1) @ A @ S
        transformed = T_inv @ A_arr @ S_arr
        
        return transformed.tolist()
        
    except (np.linalg.LinAlgError, ValueError, TypeError):
        return -1