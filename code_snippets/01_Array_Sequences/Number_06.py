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
    # checking edge case
    if len(arr) == 0:
        return 0

    # defining max and current sum and assign first element to them
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


def main():
    # testing large_cont_sum function
    print(f"arr = [8] , largest continuous sum --> {large_cont_sum([8])}")

    print(f"arr = [1, 2, -3, 10, -8, -5, 4, 7, 2, 9, -6] , "
          f"largest continuous sum --> {large_cont_sum([1, 2, -3, 10, -8, -5, 4, 7, 2, 9, -6])}")

    print(f"arr = [1, 2, -1, 3, 4, 10, 10, -10, -1] , "
          f"largest continuous sum --> {large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])}")


if __name__ == '__main__':
    main()
