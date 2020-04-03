"""
    Anagram Check

    Problem:
        Given two strings, check to see if they are anagrams. An anagram is when is two strings
        can be written using the exact same letters(so you can just rearrange the letters to g-
        et a different phrase or word).

        For example:
            "public relations" is an anagram of "crap built on lies"
            "client eastwood" is an anagram of "old west action"

    Note:
        Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g"

    Solutions:
        First: If two strings are equal to each other once they are sorted, then they are anagr-
               -ams of each other.
        Second: If two strings have same frequency of letters/element (meaning each letter shows
        up the same number of times in both strings), then they are anagrams of each other.

"""