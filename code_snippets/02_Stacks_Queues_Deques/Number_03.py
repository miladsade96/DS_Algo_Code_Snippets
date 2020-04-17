"""
    Implementation of Deque

    Deque methods and attributes:
        Deque() --> Creates a new deque that is empty. It needs no parameter
                    and returns an empty deque.
        addFront(item) --> Adds a new item to the front of the deque. It needs
                           the item and returns nothing.
        addRear(item) --> Adds a new item to the rear of the deque. It needs
                          the item and returns nothing.
        removeFront() --> Removes the front item from the deque. It needs no
                          parameters and returns the item. The deque is modified.
        removeRear() --> Removes the rear item from the deque. It needs no
                         parameters and return the item. The deque is modified.
        isEmpty() --> Tests to see whether the deque is empty or not. It needs
                      no parameters and returns a boolean value.
        size() --> Returns the number of items in the deque. It needs no para-
                   -meter and returns an integer
"""


class Deque(object):
    """Implementation of deque data structure"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
