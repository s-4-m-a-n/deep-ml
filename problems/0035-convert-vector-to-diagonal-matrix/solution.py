import numpy as np

def make_diagonal(x):
	# Your code here
	d = np.zeros((len(x), len(x)))
	for i in range(len(x)):
		d[i][i] = x[i]
	return d.tolist()
	