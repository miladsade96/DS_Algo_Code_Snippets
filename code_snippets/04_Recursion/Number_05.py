"""
    Reverse A String

    Problem:
        This interview question requires you to reverse the string
        using recursion. Make sure to think of the base case here.

        Note: Do not slice(string[::-1]) or use iteration, there
              must be a recursive call for the function.

    Solution:
        In order to reverse the string using recursion we need to
        consider what a base and recursive case would look like. Here
        we've set a base case to be when the length of the string we
        are passing through the function is length less than or equal
        to 1. During the recursive case we grab the first letter and
        add it on the recursive call.
"""

from unittest import TestCase, main


def reverse_str(s: str) -> str:
    """
    Reverse the string using recursion
    :param s: given string
    :return: reversed string
    """
    # Base case
    if len(s) <= 1:
        return s
    else:
        return reverse_str(s[1:]) + s[0]


class TestReverseStr(TestCase):
    def test_reverse_str(self):
        self.assertEqual(reverse_str("abc"), "cba")
        self.assertEqual(reverse_str("abc d"), "d cba")
        self.assertEqual(reverse_str("Hello"), "olleH")
        self.assertEqual(reverse_str("ab12c"), "c21ba")
        self.assertEqual(reverse_str("PythonIsAmazing"),
                         "gnizamAsInohtyP")
