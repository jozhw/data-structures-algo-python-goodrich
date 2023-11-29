# R-4.7
# Describe a recursive function for converting a string of digits into the
# integer it represents. For example, '13531' represents the integer
# 13,531


def calculate_power(x, n):
    """compute the value x ** n for integer n"""
    if n == 0:
        return 1
    else:
        partial = calculate_power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def convert_string_to_int(string: str, index: int):
    # to solve must add based on the tenths, hundredths...
    total_length = len(string)
    # calculate based on multiples of 10 in terms of the difference between
    # total length and current length
    if index == 0:
        return int(string[index]) * calculate_power(10, total_length)
    else:
        return convert_string_to_int(string, index - 1) + int(
            string[index]
        ) * calculate_power(10, total_length - index)


# the time complexity for this algorithm is O(nlogn) because of
# the calculate_power function
