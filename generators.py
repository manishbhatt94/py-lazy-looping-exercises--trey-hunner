"""Generator Expression Exercises."""

from itertools import chain, zip_longest
from math import isqrt


def sum_all(matrix):
    """Return the sum of all numbers in the given list-of-lists."""
    return sum(num for row in matrix for num in row)


# def all_together(*iterables):
#     """String together all items from the given iterables."""
#     return (item for iterable in iterables for item in iterable)


def all_together(*iterables):
    """String together all items from the given iterables."""
    return chain.from_iterable(iterables)


# def interleave(iterable1, iterable2):
#     """Return iterable of one item at a time from each list."""
#     sentinel = object()
#     return (
#         item
#         for pair in zip_longest(iterable1, iterable2, fillvalue=sentinel)
#         # Previously (for simple test cases where iterable lengths were same):
#         # for pair in zip(iterable1, iterable2)
#         for item in pair
#         if item is not sentinel
#     )


def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    sentinel = object()
    for one, two in zip_longest(iterable1, iterable2, fillvalue=sentinel):
        if one is not sentinel:
            yield one
        if two is not sentinel:
            yield two


# def deep_add(iterable):
#     """Return sum of values in given iterable, iterating deeply."""
#     total = 0
#     for item in iterable:
#         try:
#             total += deep_add(item)
#         except TypeError:
#             total += item
#     return total


def deep_add(iterable):
    """Return sum of values in given iterable, iterating deeply."""
    return sum(
        deep_add(item) if hasattr(item, "__iter__") else item for item in iterable
    )


# def parse_ranges(string):
#     """Return a list of numbers corresponding to number ranges in a string"""
#     return (
#         num
#         for range_str in string.split(",")
#         for low, high in [range_str.strip().split("-")]
#         for num in range(int(low), int(high) + 1)
#     )


def parse_ranges(string):
    """Return a list of numbers corresponding to number ranges in a string"""
    for range_str in string.split(","):
        low, high = range_str.strip().split("-")
        yield from range(int(low), int(high) + 1)


# def is_prime(candidate):
#     for n in range(2, candidate // 2):
#         if candidate % n == 0:
#             return False
#     return True


def is_prime(candidate):
    """Return True if candidate number is prime."""
    return candidate >= 2 and all(
        candidate % divisor != 0 for divisor in range(2, isqrt(candidate) + 1)
    )
