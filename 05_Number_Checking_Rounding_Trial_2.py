
# Display output using int / float

# Numbers to be rounded:
to_round = [1/1, 1/2, 2/3]
print("Numbers to round:")
print(to_round)

# Print rouned numbers
print()
print("Rounded numbers:")

for item in to_round:

    # If an item has no reminder after being divided by 1,
    # ... then print the number with no decimal places shown.
    if item % 1 == 0:
        print("{:.0f}".format(item))

    # Otherwise, print the number with one decimal place shown.
    else:
        print("{:.1f}".format(item))
