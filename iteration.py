"""Itertools exercises"""

from itertools import chain, dropwhile

# def total_length(*iterables):
#     """Return the total number of items in all given iterables."""
#     counter = 0
#     # OR: for _ in chain(*iterables):
#     for _ in chain.from_iterable(iterables):
#         counter += 1
#     return counter


def total_length(*iterables):
    """Return the total number of items in all given iterables."""
    return sum(1 for _ in chain.from_iterable(iterables))


def lstrip(iterable, strip_item):
    """Return iterable with strip_value items removed from beginning."""
    return dropwhile(lambda item: item == strip_item, iterable)
