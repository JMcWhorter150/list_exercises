string = input("Give me a string. ")
string = string.upper()
vowel_length = 5
string = string.replace("E", "E" * vowel_length)
string = string.replace("A", "A" * vowel_length)
string = string.replace("O", "O" * vowel_length)
string = string.replace("I", "I" * vowel_length)
string = string.replace("U", "U" * vowel_length)
string = string.lower()
print(string)