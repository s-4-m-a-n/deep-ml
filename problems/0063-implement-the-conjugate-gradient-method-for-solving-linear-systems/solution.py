import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	A = np.array(A)
	b = np.array(b)
	n_rows, n_cols = A.shape

	x = np.zeros(n_cols) if x0 is None else x0

	# calculate initial residual vector
	r = b - A @ x
	p = r.copy()
	for _ in range(n):
		alpha = ( r.T @ r )/ (p.T @ A @ p)
		x = x + (alpha * p)
		r_new = b - A @ x

		if np.linalg.norm(r_new) < tol:
			break
		
		beta = (r_new.T @ r_new) / (r.T @ r)
		new_p = r_new + beta * p

		p = new_p
		r = r_new

	return x


