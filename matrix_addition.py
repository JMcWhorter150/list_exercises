
matrix_one = [[2, -2], [5, 3], [3, 2]]
matrix_two = [[1, 3], [2, 4], [2, 3]]
matrix_empty = []
lst = []
first_counter = 0
while first_counter < len(matrix_one):
    lst = []
    second_counter = 0
    while second_counter < len(matrix_one[first_counter]):
        lst.append(matrix_one[first_counter][second_counter] + matrix_two[first_counter][second_counter])
        second_counter += 1
    matrix_empty.append(lst)
    first_counter += 1
print(matrix_empty)

for row_number in range(len(matrix_one)):
    row = matrix_one[row_number]
    for column_number in range(len(matrix_one[0])):
        print(f"{row_number} {column_number}")
        print(f"I want to add {matrix_one[row_number]} to {matrix_two[column_number]}")