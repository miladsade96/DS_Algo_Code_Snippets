"""
    Array Pair Sum

    Problem:
        Given an integer array, output all the unique pairs that sum up to a specific value k.
        So the input:

            pair_sum([1, 3, 2, 2], 4)

        Would return 2 pairs:

            (1, 3)
            (2, 2)

    Note: For testing purposes, change your function so it outputs the number of pairs.

    Solution:
        The O(n) algorithm uses the set data structure. We perform a linear pass from the
        beginning and for each element we check whether k-element is in the set of seen numbers.
        if it is, then we found a pair of sum k and add it to the output. if not, this element
        does't belong to a pair yet, and we add it to the set of seen element

"""