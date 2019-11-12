# Four parts
# 1. Multiply 1st list: 2 * 1 + -2 * 2
# Assign each number to a variable then do the math
# 
matrix_one = [[1, 3], [2, 4], [2, 5]]
matrix_two = [[1, 3, 2, 2], [2, 4, 5, 1]]
top_left = matrix_one[0][0] * matrix_two[0][0] + matrix_one[0][1] * matrix_two[1][0]
top_right = matrix_one[0][0] * matrix_two[0][1] + matrix_one[0][1] * matrix_two[1][1]
bottom_left = matrix_one[1][0] * matrix_two[0][0] + matrix_one[1][1] * matrix_two[1][0]
bottom_right = matrix_one[1][0] * matrix_two[0][1] + matrix_one[1][1] * matrix_two[1][1]
new_matrix = [[top_left, top_right], [bottom_left, bottom_right]]
print(new_matrix)

# or
a1 = matrix_one[0][0]
a2 = matrix_one[0][1]
a3 = matrix_one[1][0]
a4 = matrix_one[1][1]
b1 = matrix_two[0][0]
b2 = matrix_two[0][1]
b3 = matrix_two[1][0]
b4 = matrix_two[1][1]
tl = a1 * b1 + a2 * b3
tr = a1 * b2 + a2 * b4
bl = a3 * b1 + a4 * b3
br = a3 * b2 + a4 * b4
new_matrix2 = [[tl, tr], [bl, br]]
print(new_matrix2)
# or
# number of rows = len(big_list)
# number of columns = len(small_lists)
column_num_matrix_two = len(matrix_two[0])
row_num_matrix_one = len(matrix_one)
column_num_matrix_one = len(matrix_one[0])
row_num_matrix_two = len(matrix_two)
if column_num_matrix_one == row_num_matrix_two:
    matrix_new2 = [[0 for x in range(column_num_matrix_two)] for y in range(row_num_matrix_one)]
    for i in range(row_num_matrix_one):
        for j in range(column_num_matrix_two):
            for k in range(row_num_matrix_two):
                matrix_new2[i][j] += matrix_one[i][k] * matrix_two[k][j]
    print(matrix_new2)
else:
    print("The number of columns in matrix one does not equal the number of rows in matrix two. The multiplication of these matrices is undefined.")          

new_matrix3 = [x for x in range(column_num_matrix_two)]
print(new_matrix3)