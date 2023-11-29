# R-4.1
# Describe a recursive algorithm for finding the maximum element in a
# sequence, S, of n elements. What is your running time a space usage?


def get_max(current_max: int, index: int, array: list):
    # given an unsorted array with out any sorting algorithms,
    # start from end to beginning
    if index == -1:
        return current_max
    if current_max < array[index]:
        return get_max(array[index], index - 1, array)
    else:
        return get_max(current_max, index - 1, array)


# this algorithm's running time is O(n).
