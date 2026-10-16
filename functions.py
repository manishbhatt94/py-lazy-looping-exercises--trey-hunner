"""Generator Function Exercises."""
import math


def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


# =%=%=%=%=%=%=%=%=%=%=%=%    float_range    =%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=%

# def float_range(*args):
#     """Return iterable of numbers from start to stop by step."""
#     n = len(args)
#     if n == 1:
#         start, stop, step = 0, args[0], 1
#     elif n == 2:
#         start, stop, step = args[0], args[1], 1
#     elif n == 3:
#         start, stop, step = args
#     else:
#         raise TypeError(
#             f"range expected at least 1 argument, got {n}" if n == 0
#             else f"range expected at most 3 arguments, got {n}"
#         )
#     current = start
#     while current < stop:
#         yield current
#         current += step


# def float_range(*args):
#     """Return iterable of numbers from start to stop by step."""
#     n = len(args)
#     if n == 1:
#         start, stop, step = 0, args[0], 1
#     elif n == 2:
#         start, stop, step = args[0], args[1], 1
#     elif n == 3:
#         start, stop, step = args
#     else:
#         raise TypeError(
#             f"range expected at least 1 argument, got {n}" if n == 0
#             else f"range expected at most 3 arguments, got {n}"
#         )

#     def float_range_generator():
#         current = start
#         while current < stop:
#             yield current
#             current += step

#     return float_range_generator()


class float_range:
    def __init__(self, *args):
        n = len(args)
        if n == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif n == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif n == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(
                f"float_range expected at least 1 argument, got {n}"
                if n == 0
                else f"float_range expected at most 3 arguments, got {n}"
            )
        if self.step == 0:
            raise ValueError("float_range() arg 3 must not be zero")

    def __iter__(self):
        current = self.start
        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        else:
            while current > self.stop:
                yield current
                current += self.step

    def __len__(self):
        if self.step > 0 and self.start >= self.stop:
            return 0
        if self.step < 0 and self.start <= self.stop:
            return 0
        return math.ceil((self.stop - self.start) / self.step)


# =%=%=%=%=%=%=%=%=%=%=%=%   END float_range    =%=%=%=%=%=%=%=%=%=%=%=%=%=%=%=


def head(iterable, *, n):
    """Return first n items of a given iterable."""
    if n < 1:
        return
    consumed = 0
    for item in iterable:
        if consumed == n:
            break
        yield item
        consumed += 1


def pairwise():
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """


def around():
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """


def stop_on():
    """Yield from the iterable until the given value is reached."""


def deep_flatten():
    """Flatten an iterable of iterables."""


def get_primes_over():
    """Return given number of primes over 1,000,000."""
