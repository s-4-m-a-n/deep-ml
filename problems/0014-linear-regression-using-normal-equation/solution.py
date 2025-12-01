import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)

	XT_X_inv = np.linalg.inv(X.T @ X)
	theta = XT_X_inv @ X.T @ y
	return theta