
# Function takes in value, does conversion and puts answer into a list

# (An initial version of this piece of code was made from scratch
# by Kahlil, using a Test Plan as reference)

# Define test_input list
test_celsius_input = [0, 40, 100]

# For loop to convert each value
for item in test_celsius_input:

    # Defining degrees_c
    degrees_c = item

    # Fahrenheit output calculated using equation
    fahrenheit_output = (degrees_c * 9 / 5) + 32

    # Output Fahrenheit output variable
    print("{}°C is {}°F".format(degrees_c, fahrenheit_output))
