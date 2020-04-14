"""
    Unique characters in string

    Problem:
        Given a string, determine if it is comprised of all unique characters.
        For example, 'abcde' has all unique characters and should return true.
        The string 'aabcde' contains duplicate characters ad should return false.

    Solution:
        First: Using set data structure and built in function.
        Second : Using set data structure and our own look up function.
"""


def uni_char_1(s: str) -> bool:
    """
    Implementation of first solution
    :param s: Given string
    :return: Either True or False
    """
    return len(set(s)) == len(s)


def uni_char_2(s: str) -> bool:
    """
    Implementation of second solution
    :param s: Given string
    :return: Either True or False
    """
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


def main():
    # Testing first solution
    print(" Testing uni_char_1() function ".center(50, '*'))
    print(f"string: 'abcde' --> output: {uni_char_1('abcde')}")
    print(f"string: 'abcdde' --> output: {uni_char_1('abcdde')}")

    print("\n")

    # Testing second solution
    print(" Testing uni_char_2() function ".center(50, '*'))
    print(f"string: 'abcde' --> output: {uni_char_2('abcde')}")
    print(f"string: 'abcdde' --> output: {uni_char_2('abcdde')}")


if __name__ == '__main__':
    main()
