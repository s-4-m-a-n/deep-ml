import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    # Your code here
    basis = []
    for v in vectors:
        for e in basis:
            v = np.array(v)
            v = v - (v @ e) * e
        
        if np.linalg.norm(v) > tol:
            v = v / np.linalg.norm(v)
            basis.append(v.copy())
        
    return basis
    