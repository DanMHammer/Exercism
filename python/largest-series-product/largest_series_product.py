"""Import "reduce" in order to find the product of a slice."""
from functools import reduce


def largest_product(series, size):
    """Find the largest product of a set of 'size' consecutive digits."""
    if 1 > size >= 0:
        return 1
    if size < 0:
        raise ValueError("Size must not be negative!")
    if size > len(series):
        raise ValueError("Size must be less than or equal to series length.")

    max_product = 0
    series_int = [int(char) for char in series]

    for x in range(0, len(series)-size + 1):
        product = reduce((lambda x, y: x*y), series_int[x:x+size])
        if product > max_product:
            max_product = product

    return max_product
