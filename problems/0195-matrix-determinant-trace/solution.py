def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix (2x2 or 3x3).
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    def compute_2d_det(m: list[list[float]]) -> float:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    
    n_rows = len(matrix)
    
    if n_rows == 2:
        det = compute_2d_det(matrix)

    elif n_rows == 3:
        # Extract submatrices (minors) for Laplace expansion across row 0
        sub_00 = [
            [matrix[1][1], matrix[1][2]],
            [matrix[2][1], matrix[2][2]]
        ]
        sub_01 = [
            [matrix[1][0], matrix[1][2]],
            [matrix[2][0], matrix[2][2]]
        ]
        sub_02 = [
            [matrix[1][0], matrix[1][1]],
            [matrix[2][0], matrix[2][1]]
        ]

        det = (
            matrix[0][0] * compute_2d_det(sub_00)
            - matrix[0][1] * compute_2d_det(sub_01)
            + matrix[0][2] * compute_2d_det(sub_02)
        )
    else:
        raise NotImplementedError("Only 2D or 3D square matrix is supported")
    
    trace = sum(matrix[i][i] for i in range(n_rows))
    
    return det, trace