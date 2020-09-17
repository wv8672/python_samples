hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]

# Looping through the values in a list
for hobby in hobbies:
    print(hobby)
    print("-------------")

# range(start, stop) allows you to loop through a range of numbers
# start is the starting value (inclusive), stop is the end value (not inclusive)
for x in range(2, 5):
    print(x)
    # can reference element in list at index x
    print(hobbies[x])
print("-------------")

# Using enumeration loops through a list and creates a counter to reference the current iteration of the loop
# `index` is an integer which points to the current iteration of the loop
# Index can be named anything - it's a variable.
# `hobby` holds the value of the current element in the `hobbies` list
for index, hobby in enumerate(hobbies):
    print(hobby + " is my #" + str(index) + " hobby")
    print("-------------")
# The enumerate() function allows me to choose what number to start counting from. 
for index, hobby in enumerate(hobbies, start=1):
    print(hobby + " is my #" + str(index) + " hobby")
    print("-------------")