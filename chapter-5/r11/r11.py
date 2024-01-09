"""R-5.11: Use standard control structures to compute the sum of all numbers in
an nxn data set, represented as a list of lists"""


def sum_array(arrays: list):
    # is there a way to void a O(n^2) time complexity?
    # the simplist solution is nested loops
    total = 0
    for array in arrays:
        for value in array:
            total += value
    return total
