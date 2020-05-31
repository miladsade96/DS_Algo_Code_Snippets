"""
    Coin change problem

    Problem:
        This problem is common enough that is actually has its own wikipedia page!
        Let's check it out: https://en.wikipedia.org/wiki/Change-making_problem)

        This is a classic recursion problem: Given a target amount n and a list (array)
        of distinct coin values, what's the fewest coins needed to make the change amount.

        For Example:
            If n = 10 and coins = 1,5,10. Then there are 4 possible ways to make change:
                1. 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
                2. 5 + 1 + 1 + 1 + 1 + 1
                3. 5 + 5
                4. 10
            With 1 coin being the minimum amount.
"""

# importing relevant libraries
import pytest
from functools import lru_cache


@lru_cache(maxsize=1024)
def recursive_coin(target: int, coins: tuple) -> int:
    """
    Implementation of recursive solution
    :param target: target value
    :param coins: list of all available coins
    :return: minimum number of coins
    """
