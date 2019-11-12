matrix_one = [[2, 2, 2], [2, 2, 2]]
matrix_two = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
column_num_matrix_one = len(matrix_one[0])
row_num_matrix_one = len(matrix_one)
column_num_matrix_two = len(matrix_two[0])
row_num_matrix_two = len(matrix_two)

if column_num_matrix_one == row_num_matrix_two:
    new_matrix = [[0 for x in range(column_num_matrix_two)] for y in range(row_num_matrix_one)]
    for i in range(row_num_matrix_one):
        for j in range(column_num_matrix_two):
            for k in range(row_num_matrix_two):
                new_matrix[i][j] += matrix_one[i][k] * matrix_two[k][j]
    print(new_matrix)
else:
    print("The number of columns in matrix one do not equal the number of rows from matrix two, so the matrix product is undefined.")