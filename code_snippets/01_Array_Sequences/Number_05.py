"""
    Find The Missing Element

    Problem:
        Consider an array of non-negative integers. A second array is formed by shuffling
        the elements of the first array and deleting a random element. Given these two a-
        -rrays, find which element is missing in second array.

        Here is an example of input, the first array is shuffled  and the number 5 is re-
        moved to construct the second array.

        Input:
            finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

        output:
            5 is the missing number.

    Solution:
        The naive solution is go through every element in the second array and check whe-
        -ther it appears in the first array. Note that there may be duplicate elements in
        the arrays so we should pay special attention to it. The complexity of this appr-
        -oach is O(N^2), since we would need two for loops.

        A more efficient solution is to sort the first array, so while checking whether an
        element in the first array appears in the second, we can do binary search. But we
        should still be careful about duplicate elements. The complexity is O(NlogN).

        If we don’t want to deal with the special case of duplicate numbers, we can sort
        both arrays and iterate over them simultaneously. Once two iterators have different
        values we can stop. The value of the first iterator is the missing element. This
        solution is also O(NlogN).

        In most interviews, you would be expected to come up with a linear time solution.
        We can use a hashtable and store the number of times each element appears in the
        second array. Then for each element in the first array we decrement its counter.
        Once hit an element with zero count that’s the missing element.
"""

# importing relevant libraries
from collections import defaultdict


def finder_1(arr1: list, arr2: list) -> int:
    """
    First approach to solve the problem
    :param arr1: given first list
    :param arr2: given second list
    :return: missing element
    """
    # sort the arrays
    arr1.sort()
    arr2.sort()

    # compare elements in the sorted arrays
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    # otherwise return last element
    return arr1[-1]


def finder_2(arr1:list, arr2: list) -> int:
    pass