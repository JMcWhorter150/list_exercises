# How do I define a list?
grocery_list = ["eggs", "milk", "bread"]

# How do I get the length of a list?
len(grocery_list)

# How do I access a single item in a list?
grocery_list[1]

# How do I add stuff to a list?
grocery_list.append("beer")
grocery_list.append("cat food")

# How do I access multiple items in a list?
grocery_list[0:3]

# How do I access the last item in a list?
grocery_list[-1]

# What is "iteration" and how do I do that with a list?
for item in grocery_list:
    print(f"You need to buy {item}")

# How do I replace stuff in a list?
grocery_list[1] = "almond milk"

# How do I change multiple things in a list?
for item in range(len(grocery_list)):
    grocery_list[item] = "awesome " + grocery_list[item]

# How do I remove things from a list?
grocery_list.pop()

# How do I combine two lists?
index = 0
snacks = ["corn chips", "skittles", "oreos"]
while index < len(snacks):
    grocery_list.append(snacks[index])
    index += 1
# or
for item in range(len(snacks)):
    grocery_list.append(snacks[item])
# or
grocery_list = grocery_list + snacks

# How do I create a list of lists?
new_list = [grocery_list, snacks]


# How do I access items in a list.. that's inside anotehr list?
