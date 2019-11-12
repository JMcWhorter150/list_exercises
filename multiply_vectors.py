lst1 = [2, 4, 5]
lst2 = [2, 3, 6]
i = 0
new_lst = []
for number in lst1:
    new_lst.append(lst2[i] * number)
    i += 1
print(new_lst)
