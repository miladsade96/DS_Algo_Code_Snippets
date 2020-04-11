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


def rev_word_3(s: str) -> str:
    """
    Implementation of manually doing the splits on the spaces
    :param s: Given string
    :return: Reversed string
    """
    words = []
    length = len(s)
    spaces = [" "]

    i = 0
    while i < length:
        if s[i] not  in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start: i])
        i += 1
    return " ".join(reversed(words))


def main():
    sample_string_1 = "    How are you?"
    sample_string_2 = "if you can imagine it, so you can do it"
    sample_string_3 = "What are you doing?    "

    # Testing rev_word_1() function
    print(" Testing rev_word_1 ".center(50, "*"))
    print(f"'     How are you?' --> reversed ---> "
          f"{rev_word_1(sample_string_1)}")
    print(f"'if you can imagine it, so you can do it' --> reversed ---> "
          f"{rev_word_1(sample_string_2)}")
    print(f"'What are you doing?    ' --> reversed ---> "
          f"{rev_word_1(sample_string_3)}")
    print("\n")
    # Testing rev_word_2() function
    print(" Testing rev_word_2 ".center(50, "*"))
    print(f"'     How are you?' --> reversed ---> "
          f"{rev_word_2(sample_string_1)}")
    print(f"'if you can imagine it, so you can do it' --> reversed ---> "
          f"{rev_word_2(sample_string_2)}")
    print(f"'What are you doing?    ' --> reversed ---> "
          f"{rev_word_2(sample_string_3)}")
    print("\n")
    # Testing rev_word_3() function
    print(" Testing rev_word_3 ".center(50, "*"))
    print(f"'     How are you?' --> reversed ---> "
          f"{rev_word_3(sample_string_1)}")
    print(f"'if you can imagine it, so you can do it' --> reversed ---> "
          f"{rev_word_3(sample_string_2)}")
    print(f"'What are you doing?    ' --> reversed ---> "
          f"{rev_word_3(sample_string_3)}")


if __name__ == '__main__':
    main()
