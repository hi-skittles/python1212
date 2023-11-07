from colours import colours as c


def __init__():
    pass


def __main__():
    pass


def __name__():
    return "__main__"


#  print('Problem 1', end='\n\n----------\n')
#  print('----------', end='\n\n')
def top(problem: int) -> str:
    return f"\nProblem {problem}\n----------\n{c.OKGREEN}"


def bottom() -> str:
    return f"{c.ENDC}\n----------\n"
