from colours import *

"""
The first value, before the first colon (:), represents the starting index.
The second value, between the first and second colons, represents the ending index (exclusive).
The third value, after the second colon (:), represents the step size, which determines the spacing between elements to include.
"""


# Problem 1
def add(a: int, b: int) -> int:
    """
    Adds a to b.
    :param a: int
    :param b: int
    :return: int
    """
    return a + b


# Problem 2
def iseven(a: int) -> bool:
    """
    Checks if a is even.
    :param a: int
    :return: bool
    """
    return a % 2 == 0


# Problem 3
def get_even(foo: list) -> list:
    """
    Gets even numbers from a list, without duplicates.
    :param foo: list
    :return: list
    """
    bar = [i for i in foo if i % 2 == 0]
    # res = []
    # [res.append(x) for x in bar if x not in res]
    return list(set(bar))  # preservation is not a priority here


# Problem 4
def get_min_even(a: list, b: int) -> list:
    """
    Takes a list and given parameter and outputs a new list of numbers that are even and greater than b.
    :param a: list
    :param b: int
    :return: list
    """
    foo = [i for i in a if i % 2 == 0 and i > b]
    return list(set(foo))  # preservation is not a priority here


# Problem 5
def word_count(a: str) -> int:
    """
    Counts the number of words in a string.
    :param a: str
    :return: int
    """
    return len(a.split(' '))


question = input('Which problem would you like to run?: ')
if question.isdigit():
    match question:
        case '1':
            print(add(-1, 98))
            print(add(1, 6))
        case '2':
            print(iseven(56))
            print(iseven(1))
            print(iseven(55))
        case '3':
            print(get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 12, 12, 1029, 109]))
        case '4':
            print(get_min_even(list(range(1, 120))[::1], 2))
        case '5':
            print(word_count("From a programmer’s point of view the user is a peripheral that types when you issue a "
                             "read request"))
        # case '6':
        #     six()
        case _:  # default
            print('Invalid problem number.')
