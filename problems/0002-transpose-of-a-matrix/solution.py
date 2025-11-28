def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    t_a = []
    for i in range(len(a[0])): # column wise
        t_row = []
        for j in range(len(a)): # row wise
            t_row.append(a[j][i])
        t_a.append(t_row)
        t_row = []

	return t_a