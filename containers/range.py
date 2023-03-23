def range(a, b=None, c=None):
    '''
    This function should behave exactly like
    the built-in range function!
    For example:
    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''

    if b is None and c is None:
        d = 0
        while d < a:
            yield d
            d += 1
    elif c is None:
        d = a
        while d < b:
            yield d
            d += 1
    else:
        d = a
        if c > 0:
            while d < b:
                yield d
                d += c
        else:
            while d > b:
                yield d
                d += c
