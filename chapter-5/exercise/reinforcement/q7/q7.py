"""R-5.7: Let A be an array of size n >= 2 containing integers from 1
to n-1, inclusive, with exactly one repeated. Describe a fast algorithm
for finding the integer in A that is repeated."""


def find_repeat(array):
    """find a repeating value given that there is only one repeating value
    to most efficient solution is to create a array of falsey and set true
    to each falsey
    another way to do this is create a hashtable of all of the values
    of the array and set each one to false and iterate through the array
    and set each value to true and if it is true previously then it is
    a duplicate. the issue with this solution is that it relies on the
    dynamic array because the value within the array may be greater than the
    length of the array when it is initialized; however given the efficiency
    of dynamic arrays, it is a efficient solution."""
    comparison_array = len(array) * [False]
    for value in array:
        if comparison_array[value]:
            return value
        else:
            comparison_array[value] = True
