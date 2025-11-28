def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = []
    for i in range(len(matrix)):
        result.append(
            [j*scalar for j in matrix[i]]
        )
            
	return result