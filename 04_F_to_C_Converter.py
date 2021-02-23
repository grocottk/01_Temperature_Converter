
# Function takes in value, does conversion and puts answer into a list

# (An initial version of this piece of code was made from scratch
# by Kahlil, using a Test Plan as reference)

# Define test_input list
test_fahrenheit_input = [0, 32, 100]
converted_to_celsius = []

# For loop to convert each value
for item in test_fahrenheit_input:

    # Defining degrees_f
    degrees_f = item

    # Celsius output calculated using equation
    celsius_output = (degrees_f - 32) * 5/9

    # Adds converted values to "converted_to_celsius" list
    converted_to_celsius.append(celsius_output)

    # Output celsius output variable
    print("{}°F is {:.2f}°C".format(degrees_f, celsius_output))

# Prints raw converted data
print("Raw Data: {} (all in degrees celsius)".format(converted_to_celsius))
