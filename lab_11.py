from colours import colours
from headers import top as header_top, bottom as header_bottom
from typing import Union, List

"""
The first value, before the first colon (:), represents the starting index.
The second value, between the first and second colons, represents the ending index (exclusive).
The third value, after the second colon (:), represents the step size, which determines the spacing between elements to include.
"""


# Problem 1
def add(a: int or float, b: int or float) -> int or float:  # not using Unions to reduce imports
    """
    Adds a to b, not including strings.

    :param a: int or float
    :param b: int or float
    :return: int or float
    """
    return a + b


# Problem 2
def iseven(a: Union[int, float]) -> bool:
    """
    Checks if a is even.

    :param a: int or float
    :return: bool
    """
    return a % 2 == 0


# Problem 3
def get_even(foo: List[int]) -> List[int]:
    """
    Gets even numbers from a list, without duplicates.

    :param foo: List of integers
    :return: List of unique even integers
    """
    return list(set(i for i in foo if i % 2 == 0))  # Instead of creating a list and then converting it to a set to
    # remove duplicates, you can directly use a set comprehension to ensure unique elements.


# Problem 4
def get_min_even(a: List[int], b: int) -> List[int]:
    """
    Returns a list of unique even numbers from the input list that are greater than b.    :param a: list

    :param a: List of integers
    :param b: Minimum threshold level
    :return: List of unique even integers greater than b
    """
    return list(set(i for i in a if i % 2 == 0 and i > b))


# Problem 5
def word_count(a: str) -> int:
    """
    Counts the number of words in a string.
    :param a: str
    :return: int
    """
    return len(a.split())  # splitting at ' ' does not account for whitespaces and indents


question = input('Which problem would you like to run?: ')
if question.isdigit():
    match question:
        case '1':
            print(f'{header_top(1)}{add(-1, 98)}\n{add(1, 6)}{header_bottom()}')
        case '2':
            print(f'{header_top(2)}{iseven(56)}\n{iseven(1)}\n{iseven(55)}{header_bottom()}')
        case '3':
            print(f'{header_top(3)}{get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 12, 12, 1029, 109])}{header_bottom()}')
        case '4':
            print(f'{header_top(4)}{get_min_even(list(range(0, 1001))[::5], 0)}{header_bottom()}')
        case '5':
            print(f'{header_top(5)}{word_count(input("Enter some words: "))}{header_bottom()}')
        case _:  # default
            print(f'{colours.WARNING}Invalid problem number.')
else:
    print(f'{colours.WARNING}Invalid problem number.')
