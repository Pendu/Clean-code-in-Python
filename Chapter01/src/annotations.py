"""Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

> Annotations
"""


class Point:  # pylint: disable=R0903
    """Example to be used as return type of locate"""
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


def locate(latitude: float, longitude: float) -> Point:
    """By mentioning the input variable type and return type for this method,
       the function is now statically typed, not dynamically typed. Now we can
       use mypy. check first page of mypy documentation to understand this further"""
    """Find an object in the map by its coordinates"""
    return Point(latitude, longitude)


class NewPoint:  # pylint: disable=R0903
    """Example to display its __annotations__ attribute."""
    lat: float
    long: float
