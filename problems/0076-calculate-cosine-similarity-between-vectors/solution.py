
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	dot = v1 @ v2
    v1_norm = (v1 @ v1)**0.5
    v2_norm = (v2 @ v2)**0.5
    return np.round(dot/(v1_norm * v2_norm), 3)
