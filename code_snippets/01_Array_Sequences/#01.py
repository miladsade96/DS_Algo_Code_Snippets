"""
    Code snippet in order to experiment and explore the relationship between
    list length and underlying size that the computer holding in memory.
"""

import sys

# Setting n
n = 50

# Creating an empty list named `data`
data = []

for i in range(n):
    # Number of elements
    a = len(data)

    # Actual size of bytes
    b = sys.getsizeof(data)

    print("Length: {0:3d}; size in bytes: {1:4d}".format(a, b))

    # Increase length by one
    data.append(n)