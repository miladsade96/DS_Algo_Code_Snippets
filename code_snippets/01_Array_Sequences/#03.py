"""
    Anagram Check

    Problem:
        Given two strings, check to see if they are anagrams. An anagram is when is two strings
        can be written using the exact same letters(so you can just rearrange the letters to g-
        et a different phrase or word).

        For example:
            "public relations" is an anagram of "crap built on lies"
            "clint eastwood" is an anagram of "old west action"

    Note:
        Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g"

    Solutions:
        First: If two strings are equal to each other once they are sorted, then they are anagr-
               -ams of each other.
        Second: If two strings have same frequency of letters/element (meaning each letter shows
                up the same number of times in both strings), then they are anagrams of each other.

"""


def anagram_1(s1: str, s2: str) -> bool:
    """Implementation of first solution"""
    # Remove whitespaces and lowercase all letters
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


def anagram_2(s1: str, s2: str) -> bool:
    """Implementation of second solution"""
    # Remove and lowercase all letters
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Edge case check
    if len(s1) != len(s2):
        return False

    # Defining an empty dictionary
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


def main():
    # Testing anagram_1
    print(" Testing anagram_1 function ".center(50, "*"))
    print(f"'god' is an anagram of 'dog': {anagram_1('god', 'dog')}")
    print(f"'clint eastwood' is an anagram of 'old west action':"
          f"{anagram_1('clint eastwood', 'old west action')}")

    print("\n")

    # Testing anagram_2
    print(" Testing anagram_2 function ".center(50, "*"))
    print(f"'god' is an anagram of 'dog': {anagram_2('god', 'dog')}")
    print(f"'clint eastwood' is an anagram of 'old west action':"
          f"{anagram_2('clint eastwood', 'old west action')}")


if __name__ == '__main__':
    main()
