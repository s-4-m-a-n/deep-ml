import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.

	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	A = np.array(A)
	m, n = A.shape

	b = np.array(b)
	if n != len(b):
		raise ValueError("length of the column of A and length of b should be equal")

	# augmented matrix [A | b]
	M = np.column_stack([A, b])
	pivot_row = 0

	# ========== forward elimination ========
	for c in range(n):
		if pivot_row > m:
			break
		
		# find max value pivot
		pivot_offset = np.argmax(np.abs(M[pivot_row:, c]))
		new_pivot_row = pivot_row + pivot_offset

		if np.abs(M[new_pivot_row, c]) < 1e-10:
			continue
		
		# swap the row with max pivot value row
		M[[pivot_row, new_pivot_row]] = M[[new_pivot_row, pivot_row]]

		# eliminate all the value below pivot row
		for r in range(pivot_row+1, m):
			factor = M[r, c] / M[pivot_row, c]
			M[r] = M[r] - factor * M[pivot_row] 
		
		pivot_row += 1
	# ===== backward substitution =======
	x = np.zeros(n)
	for row in range(n-1, -1, -1):
		# sum of already known variable
		known = np.dot(M[row, row + 1:n], x[row + 1:n])
		x[row] = (M[row, -1] - known) / M[row, row]

	return x
