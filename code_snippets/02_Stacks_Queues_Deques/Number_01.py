"""
    Implementation of stack

    Stack attributes and methods:
        Stack() --> Creates a new stack that is empty. It needs no parameters
            and returns an empty stack.
        push(item) --> Adds a new item to the top of the stack. It needs the
            item and return nothing.
        pop() --> Removes the top item from the stack. It needs no parameters
            and returns the item. The stack is modified.
        peek() --> Returns the top item from the stack but foes not remove it.
            It needs no parameters. The stack is not modified.
        isEmpty() --> Tests to see whether the stack is empty or not. It needs
            no parameters and returns a boolean value.
        size() --> Returns the number of items on the stack. It needs no para-
            -meters and returns an integer.
"""


class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []