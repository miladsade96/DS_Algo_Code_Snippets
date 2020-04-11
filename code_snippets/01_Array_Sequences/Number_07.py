"""
    Sentence Reversal

    Problem:
        Given a string of words, reverse all the words.
        For Example:
            Input --> "This is the best"
            Output --> "best the is This"

    Note: As part of ths exercise, you should remove all leading and trailing
          whitespaces. So that inputs such as:
                "   space here" and "space here     "
          both become:
                "here space"

    Solution:
        We could take advantage of python's abilities and solve the problem with
        the use of split() and some slicing or use of reversed.
"""


def rev_word_1(s: str) -> str:
    """
    Implementation of solution using join, split and reversed
    :param s: Given string
    :return: Reversed string
    """
    return " ".join(reversed(s.split()))


def rev_word_2(s: str) -> str:
    """
    Implementation of solution using join, split and slicing
    :param s: Given string
    :return: Reversed string
    """
    return " ".join(s.split()[::-1])
