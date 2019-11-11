my_string = "abracadabra"
new_string = ""
index = 0
while index < len(my_string):
    # print(my_string[-1 + -1 * index])
    # working through a negative indexing route. Start at -1 + 0, then -1 + -1, etc.
    new_string += (my_string[len(my_string) - 1 - index])
    # -1 because len str outside index range cause indexing starts at 0
    index += 1
print(new_string)