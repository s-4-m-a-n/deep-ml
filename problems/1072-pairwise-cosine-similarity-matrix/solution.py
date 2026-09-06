import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X)
    dot = X @ X.T
    l2_norms = np.linalg.norm(X, ord=2, axis=1, keepdims=True)
    l2_norms[l2_norms==0] = 1.0
    return (dot/(l2_norms @ l2_norms.T)).tolist()