"""
    Problem:
        Implementation of fibonacci sequence in three different ways:
            * Recursively
            * Iteratively
            * Dynamically (Using memoization to store results)

    Note: Your function should accept a number n and return the nth
          number of the fibonacci sequence.
"""

# import relevant libraries
from unittest import TestCase, main


def recursive_fib(n: int) -> int:
    """
    Implementation of fibonacci sequence using recursion
    :param n: given integer number
    :return: nth number of fibonacci sequence
    """
    # Base case
    if n == 0 or n == 1:
        return n
    # recursive part
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def iterative_fib(n: int) -> int:
    """
    Implementation of fibonacci sequence using iteration
    :param n: Given integer number
    :return: nth number of fibonacci sequence
    """
    pass