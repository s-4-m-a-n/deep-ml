def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "row":
        for i in range(len(matrix)):
            mean = 0
            for j in matrix[i]:
                mean += j
            mean /= len(matrix[i])
            means.append(mean)
            mean = 0
    else:
        for i in range(len(matrix[0])):
            mean = 0
            for j in range(len(matrix)):
                mean += matrix[j][i]
            mean /= len(matrix)
            means.append(mean)
            mean = 0
	return means