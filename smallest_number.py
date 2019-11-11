my_list = [1, 4, 7, 3, 8, 14, 19, 0, -1]
smallest_number = 0
for number in my_list:
    if number <= smallest_number:
        smallest_number = number
print(smallest_number)