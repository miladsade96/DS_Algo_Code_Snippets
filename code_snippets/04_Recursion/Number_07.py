"""
    Problem:
        Implementation of fibonacci sequence in three different ways:
            * Recursively
            * Iteratively
            * Dynamically (Using memoization to store results)

    Note: Your function should accept a number n and return the nth
          number of the fibonacci sequence.
"""


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
    # start point
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


# Dynamically
# cache information
cache = {}


def dynamic_fib(num: int) -> int:
    """
    Implementation of fibonacci sequence using dynamic programming
    :param num: Given integer number
    :return: nth number of fibonacci sequence
    """
    # checking cache
    if num in cache:
        return cache[num]

    # Base case
    if num == 0 or num == 1:
        return num
    else:
        value = dynamic_fib(num - 1) + dynamic_fib(num - 2)
    cache[num] = value
    return value
