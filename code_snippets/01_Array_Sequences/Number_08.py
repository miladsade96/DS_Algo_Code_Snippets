"""
    String Compression

    Problem:
        Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become
        'A4B4C5D2E4'. For this problem, you can falsely 'compress' strings of
        single or double letters. For instance it is ok for 'AAB' to return
        'A2B1' even though this technically takes more space.

        The function should also be case sensitive, so that a string 'AAAaaa'
        returns 'A3a3'.

    Solution:
        Since python strings are immutable, we will need wok off of a list of
        characters, and at the end convert that list back into a string with
        a join statement.
"""


def compress(s: str) -> str:
    """
    Implementation of the solution
    :param s: Given string
    :return: Returned string including counts for characters
    """
    r = ""
    l = len(s)

    if l == 0:
        return ""
    elif l == 1:
        return s + "1"
