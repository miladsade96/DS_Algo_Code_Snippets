"""
    Problem:
        Create a function called word_split which takes in a string phrase
        and a set list_of_words. The function then will determine if it is
        possible to split the string in a way in which words can be made from
        the list of words. You can assume the phrase will only contain words
        found in a dictionary if it is completely splittable.
"""
# importing relevant libraries
from typing import List, AnyStr


def word_split(phrase: AnyStr, list_of_words: List, output=None) -> List:
    """
    Implementation of solution
    :param phrase: given string
    :param list_of_words: list containing the words
    :param output: output parameter to initiate in every recursion
    :return: a list of words
    """
    # check to see any output has been initiated
    if output is None:
        output = []
    # for every word in the list
    for word in list_of_words:
        # if the current phrase begins with the word,
        # we have a split point
        if phrase.startswith(word):
            # add the word to the output
            output.append(word)
            # recursively call the split function to the remaining
            # portion of the string
            return word_split(phrase[len(word):], list_of_words, output)
    # returning final output
    return output
