# R-4.6
# Describe a recursive function for computing the nth Harmonic number,
# H subscript n = sum from i = 1 to n of 1/i


def harmonic_sum(n: int):
    """return a sum of two harmonic number 1/n and 1/(n - 1)"""
    if n <= 1:
        return 0
    else:
        return harmonic_sum(n - 1) + 1 / n


# the time complexity is O(n)
