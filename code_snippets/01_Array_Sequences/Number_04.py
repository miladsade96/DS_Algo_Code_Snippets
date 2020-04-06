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


def pair_sum(arr: list, k: int) -> int:
    """ Implementation of array pair sum solution"""
    # return 0 if length of list is less than 2
    if len(arr) < 2:
        return 0

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return len(output)


def main():
    # Testing pair_sum()
    print(pair_sum([1, 3, 2, 2], 4))


if __name__ == '__main__':
    main()
