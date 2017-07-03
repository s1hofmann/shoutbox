#!/usr/bin/env python3

# Create a list of ints
a_list = [1, 2, 3, 4, 5, 6]

# Iterate over list and print elements
for element in a_list:
    print(element)

# Iterate over list in reverse direction and print elements
for element in reversed(a_list):
    print(element)

# Iterate over list with index elements
for index, element in enumerate(a_list):
    print("Element at index %s: %s" % (index, element))

# Combine two lists

x_coord = [10, 34, 3, 56, 110]
y_coord = [74, 2, 9, 78, 43]

for coord in zip(x_coord, y_coord):
    print("Coordinates:", coord)
