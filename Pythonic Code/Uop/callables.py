from collections import defaultdict


class CallCount:
    """
    >>> cc = CallCount()
    >>> cc(1)
    1
    >>> cc(2)
    1
    >>> cc(1)
    2
    >>> cc(1)
    3
    >>> cc("something")
    1

    >>> callable(cc)
    True
    """

    def __init__(self):
        """ default value of int is 0"""
        """A defaultdict works exactly like a normal dict, but it is
           initialized with a function (“default factory”) that takes no
           arguments and provides the default value for a nonexistent key.
           A defaultdict will never raise a KeyError. Any key that does not
           exist gets the value returned by the default factory"""
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]
