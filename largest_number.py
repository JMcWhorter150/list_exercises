my_list = [1, 4, 7, 3, 8, 14, 19, 0, -1]
biggest_number = 0
for number in my_list:
    if number >= biggest_number:
        biggest_number = number
print(biggest_number)