from colours import colours
from headers import top as header_top, bottom as header_bottom
from typing import Union, List


def one() -> None:
    """
    Prints the numbers 0, 1, and 2, each on a separate line, and then prints a triangle of exclamation marks.
    :return: None
    """
    #  i do not want to put this in return sorry :(
    n = 0
    while n < 3:
        print(n)
        n += 1

    i = 0
    while i < 3:
        j = 0
        while j < (i + 1):
            print("*", end="")
            j += 1
        print("!")
        i += 1


def two(n: int) -> List[int]:
    """
    Prints all the squares of positive integers where the square is less than or equal to the value passed in,
    in ascending order.
    :param n: int
    :return: List[int]
    """
    i = 1
    y = []
    while i ** 2 <= n:
        y.append(i ** 2)
        i += 1
    return y


def three(n: int) -> int:
    """
    Returns the smallest integer factor of n that is greater than 1.
    :param n: int
    :return: int
    """
    i = 2
    while n % i != 0:
        i += 1
    return i


def four(starting: Union[int, float], goal: Union[int, float], daily_increase: Union[int, float]) -> str:
    """
    Returns the number of days it will take to reach the goal distance.
    :param starting: int
    :param goal: int
    :param daily_increase: int
    :return: str
    """
    #  could add other checks cba out of time rn
    return f"You will reach your goal in {int(((goal - starting) / daily_increase) / 10)} days."


def five() -> None:
    return None


question = input('Which problem would you like to run?: ')
if question.isdigit():
    match question:
        case '1':
            print(f'{header_top(1)}{one()}{header_bottom()}')
        case '2':
            print(f'{header_top(2)}{two(50)}{header_bottom()}')
        case '3':
            print(f'{header_top(3)}{three(int(input("Enter a number that is greater than 0: ")))}{header_bottom()}')
        case '4':
            print(colours.OKCYAN)
            a = int(input("Enter starting distance: "))
            b = int(input("Enter goal distance: "))
            c = float(input("Enter daily increase: "))
            print(colours.ENDC)
            print(f'{header_top(4)}{four(a, b, c)}{header_bottom()}')
        case '5':
            print(f'{header_top(5)}{five()}{header_bottom()}')
        case _:  # default
            print(f'{colours.WARNING}Invalid problem number.')
else:
    print(f'{colours.WARNING}Invalid problem number.')
