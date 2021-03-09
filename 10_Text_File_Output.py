
# Source shown in ePub "Writing to File" video, which this code is based on.

# Import Regular Expression(s)

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Name Error Checking (Checks if a name is valid)
has_error = "yes"
while has_error == "yes":
    print()

    # Get file name, which can't be blank or invalid (though it is assumed that it is for now).
    file_name = input("Enter a file name (file extension not required): ")

    has_error = "no"

    valid_character = "[A-Za-z0-9_]"
    for letter in file_name:
        if re.match(valid_character, letter):
            continue

        elif letter == " ":
            problem = "Spaces are not an allowed character"

        else:
            problem = ("{} is not a valid character".format(letter))
        has_error = "yes"

    if file_name == "":
        problem = "The file name is not allowed to be blank"
        has_error = "yes"

    if has_error == "yes":
        print("This file name is not allowed: {}".format(problem))

    # If entry is valid
    else:
        print("You entered a valid file name")

# Main section of build

# Add .txt suffix
file_name = file_name + ".txt"

# Create file (to hold data)
f = open(file_name, "w+")

# Add new line at end of each item
for item in data:
    f.write(item + "\n")

# Close file
f.close()
