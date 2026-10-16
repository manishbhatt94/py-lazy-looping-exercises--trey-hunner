"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [
        name
        for name in names
        if len(name) > 0 and name[0].lower() in ['a', 'e', 'i', 'o', 'u']
    ]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [elem for row in matrix for elem in row]


def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    return [
        [ int(elem) for elem in line.split() ]
        for line in string.splitlines()
    ]


def power_list(nums):
    """Return a list that contains each number raised to the i-th power."""
    return [
        num ** index
        for index, num in enumerate(nums)
    ]


def matrix_add(m1, m2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [ sum(pair) for pair in zip(row1, row2) ]
        for row1, row2 in zip(m1, m2)
    ]


def identity(size):
    """Return an identity matrix of size x size."""
    return [
        [ 1 if row == col else 0 for col in range(size) ]
        for row in range(size)
    ]


def triples(limit):
    """Return list of Pythagorean triples less than input num."""
    return [
        (a, b, c)
        for a in range(3, limit + 1)
        for b in range(a + 1, limit + 1)
        for c in range(b + 1, limit + 1)
        if a**2 + b**2 == c**2
    ]
