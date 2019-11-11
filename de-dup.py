old_lst = [1, 2, 3, 2, 3, 4, 17, 19, 17, 0, 4, 8, 12, 4]
de_dup_lst = []
for number in old_lst:
    if number not in de_dup_lst:
        de_dup_lst.append(number)
print(de_dup_lst)