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
    # default to target value
    minimum_coins = target

    # Base case - checks to se if we have a single coin match
    if target in coins:
        return 1
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + recursive_coin(target - i, coins)
            # resetting the minimum
            if num_coins < minimum_coins:
                minimum_coins = num_coins
    return minimum_coins


def dynamic_coin(target: int, coins: tuple, known_results: list) -> int:
    """
    Implementation of dynamic solution
    :param target: target value
    :param coins: list of all available coins
    :param known_results: list of known results as cache memory
    :return: minimum number of coins
    """
    # default output to target
    minimum_coins = target

    # Base case
    if target in coins:
        known_results[target] = 1
        return 1

    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        # for every coin value that i <= than target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + dynamic_coin(target - i, coins, known_results)
            # resetting the minimum
            if num_coins < minimum_coins:
                minimum_coins = num_coins
                # reset the known result
                known_results[target] = minimum_coins
    return minimum_coins


parameters = [
    (45, (1, 5, 10, 25), 3),
    (23, (1, 5, 10, 25), 5),
    (74, (1, 5, 10, 25), 8)
]


@pytest.mark.parametrize("target, coins, expected", parameters)
def test_recursive_coin(target, coins, expected):
    assert recursive_coin(target, coins) == expected


@pytest.mark.parametrize("target, coins, expected", parameters)
def test_dynamic_coin(target, coins, expected):
    assert dynamic_coin(target, coins, known_results=[0] * (target + 1)) == expected
