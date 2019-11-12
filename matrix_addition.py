
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