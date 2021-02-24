
# Number Checker attempt

# Defining validity messages
valid = "This entry is valid"
invalid = "This entry is not valid [Continue...]"

# Asks for number
number = int(input("Please enter a number: "))

# If a number is greater than absolute zero, it is valid.
if number > -273:
    print(valid)

# If a number is greater than absolute zero, it is valid.
elif number > -459:
    print(valid)

# Otherwise, the entry is invalid, and the program continues.
else:
    print(invalid)

# Print number for testing
print(number)
