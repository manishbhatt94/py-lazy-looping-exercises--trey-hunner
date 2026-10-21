"""Iterator exercises"""

import random


def first(iterable):
    """Return the first item in given iterable."""
    iterator = iter(iterable)
    try:
        first_item = next(iterator)
    except StopIteration:
        return
    else:
        return first_item


def is_iterator(iterable):
    """Return True if given iterable is an iterator."""
    return iterable is iter(iterable)


class Point:
    """3-D Point objects"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


def all_same(iterable):
    """Return True if all items in the given iterable are the same."""
    iterator = iter(iterable)
    try:
        first_val = next(iterator)
    except StopIteration:
        return True
    return all(val == first_val for val in iterator)


def minmax(iterable):
    """Return minimum and maximum values from given iterable."""
    iterator = iter(iterable)
    try:
        first_value = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty. Cannot compute min/max.")
    else:
        min_value = first_value
        max_value = first_value
    for value in iterator:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    return (min_value, max_value)


class RandomNumberGenerator:
    """Return infinite series of randomly generator numbers.

    Infinite iterator yielding random integers in [start, end].
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"RandomNumberGenerator(start={self.start}, end={self.end})"

    def __iter__(self):
        return self

    def __next__(self):
        return random.randint(self.start, self.end)
