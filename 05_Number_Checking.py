
# Number Checker answer (to check that a number is valid)

# Number Checking Function:


def temperature_check(low):

    valid = False
    while not valid:

        try:

            response = float(input("Enter a number: "))

            if response < low:
                print("This temperature is valid (as it is lower than absolute zero)")
            else:
                return response

        except ValueError:
            print("Please enter a temperature")

# Main Routine:

# Run this code twice, in order to gain two valid responses in the test plan.
number = temperature_check(-273)
print("You chose {}".format(number))

number = temperature_check(-459)
print("You chose {}".format(number))
