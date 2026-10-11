
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot_vL = sum(vi * Li for vi, Li in zip(v, L))
	dot_LL = sum(Li * Li for Li in L)

	if dot_LL == 0:
		raise ValueError("must be non zero length")
	
	scalar = dot_vL / dot_LL
	proj_v = [scalar * Li for Li in L]
	return proj_v