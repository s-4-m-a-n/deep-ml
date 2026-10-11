
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	proj_v = [0]*len(v)
	unit_L = sum(i**2 for i in L)
	for i in range(len(v)):
		proj_v[i] = (v[i] * L[i]) * L[i]/ unit_L
	return proj_v
