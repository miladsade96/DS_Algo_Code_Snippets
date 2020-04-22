"""
    Balanced Parenthesis Check

    Problem:
        Given an string of opening and closing parenthesis, check whether it's
        balanced. We have 3 types of parenthesis: round brackets -> (), square
        brackets -> [] and curly bracket -> {}. Assume that the string doesn't
        contain any other character than these, no spaces, words or numbers. As
        a reminder, balanced parenthesis require every opening parenthesis to
        be closed in the reversed order opened.

        For Example:
            input --> ({}) is balanced,     output --> True
            input --> ({]) is'nt balanced,  output --> False

    Solution:
        First we will scan the string from left to right, and every time we see
        an opening parenthesis we push it to the stack, because we want the last
        opening parenthesis to be closed first. Then, when we see a closing par-
        -enthesis we check whether the last opened one is the corresponding clo-
        -sing match, by popping the element from stack. If it's a valid match,
        then we proceed forward, if not return false. Or if the stack is empty
        we also return false, because there is no opening parenthesis associated
        with this closing one. At the end, we also check whether the stack is
        empty. If so, we return true, otherwise return false because there were
        some opened parenthesis that were not closed.
"""