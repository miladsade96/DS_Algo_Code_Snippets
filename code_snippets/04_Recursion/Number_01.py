"""
    Implementation of factorial function using recursion

    factorial:
                n! = n * (n - 1)!
                if n = 0 --> n! = 1
"""


def factorial(n: int) -> int:
    """
    Factorial function with recursion
    :param n: given number that we are gonna find its factorial
    :return: factorial value
    """
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
