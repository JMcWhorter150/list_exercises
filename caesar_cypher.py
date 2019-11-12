string = "lbh zhfg hayrnea jung lbh unir yrnearq"
dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lst = list(string)
for number in range(26):
    new_lst = []
    shift = number
    for character in lst:
        if character == " ":
            new_lst.append(" ")
        else:
            for i in range(len(dictionary)):
                if character == dictionary[i]:
                    new_lst.append(dictionary[i + shift])
                    break
    my_string = "".join(new_lst)
    print(shift, my_string)
    # you must unlearn what you have learned