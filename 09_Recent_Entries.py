
# This code is from the file "07_most_recent_v4" by Ms. Gottschalk

# Set up empty list
all_calculations = []

# Get five items of data
get_item = ""

while get_item != "xxx":
    get_item = input("Please enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

# If no entries are present
if len(all_calculations) == 0:
    print("Oops, the list is empty")

else:

    # Show that everything made it to the list:
    print()
    print("The full list:")
    print(all_calculations)

    # Print items, starting from the end of the list,
    # ... and printing in a "backwards" direction (from newest to oldest).
    if len(all_calculations) >= 3:
        print(" Most recent three (3) entries:")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    # If three entries are not present, print all entries available,
    # ... from newest to oldest.
    else:
        print("Items from newest to oldest:")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])
