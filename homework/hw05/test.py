def hailstone(n):
    """
    Yields the elements of the hailstone sequence starting at n.
    At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        while True:
            yield 1
    elif n % 2 == 1:
        yield from hailstone(3 * n + 1)
    else:
        yield from hailstone(n / 2)
    
hail_gen = hailstone(10)
print(next(hail_gen))
