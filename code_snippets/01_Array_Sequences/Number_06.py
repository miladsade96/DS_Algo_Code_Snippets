"""
    Largest Continuous Sum

    Problem:
        Given an array of integers(positive and negative), find the largest continuous sum.

    Solution:
        If the array is all positive, then the result is simply the sum of all numbers. The
        negative numbers in the array will cause us to need to begin checking sequences.

        The algorithm is , we start summing up the numbers and store in the current sum
        variable. After adding each element, we check whether the current sum is larger
        than maximum sum encountered so far. If it is, we update the maximum sum. As long
        as current sum is positive, we keep adding the numbers. When the current sum becomes
        negative, we start with the new current sum; Because a negative current sum will
        only decrease the sum of the future sequence. Note that we don't reset the current
        sum to 0 because array can contain all negative integers. Then the result would be
        the largest negative number.
"""


def large_cont_sum(arr: list) -> int:
    """
    Implementation of largest continuous sum
    :param arr: Given an array
    :return: largest continuous sum
    """