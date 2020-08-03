import doctest

def get_slices():
    """
    >>> my_numbers = (1,2,3,4,5,6,7,8)
    >>> interval = slice(1,7,2)
    >>> my_numbers[interval]
    (2, 4, 6)
    """

def main():
    get_slices()
    fail_count, _ = doctest.testmod(verbose=True)
    raise SystemExit(fail_count)

if __name__=="__main__":
    main()