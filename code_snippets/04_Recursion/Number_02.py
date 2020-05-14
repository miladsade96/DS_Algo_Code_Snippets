"""
    Problem:
        Write a recursive function which takes an integer and
        computes the cumulative sum of 0 to that integer.

        For example:
            if n = 4 --> return 4 + 3 + 2 + 1, which is 10.

    Hint:
        In this case, we have: n + (n - 1) + (n - 2) + ... + 0
"""


def rec_sum(n: int) -> int:
    """
    Recursive sum
    :param n: given number that we're gonna sum from 0 to it
    :return: result of sum from 0 ro n
    """