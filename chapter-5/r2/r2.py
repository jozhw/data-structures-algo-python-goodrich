"""R-5.1 Redesign the experiment so that the program outputs only those values of
k at which the existing capacity is exhausted. For example
on a system consistent with the results of Code Fragment 5.2, your program should output that
the sequence of array capacities are 0, 4, 8, 16, 25, ..."""

import sys

data = []
current_mem_usage = 0
for k in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    if b > current_mem_usage:
        current_mem_usage = b
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)
