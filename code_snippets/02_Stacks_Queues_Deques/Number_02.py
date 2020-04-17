"""
    Implementation of Queue

    Queue methods and attributes:
        Queue() --> Creates a new queue that is empty. It needs no parameters
                    and returns an empty queue.
        enqueue(item) --> Adds a new item to the rear of the queue. It needs
                          the item and returns nothing.
        dequeue() --> Removes the front item from the queue. It needs no para-
                      -meter and returns the item. The queue is modified.
        isEmpty() --> Tests to see whether the queue is empty or not. It needs
                      no parameter and returns a boolean value.
        size() --> Returns the number of items in queue. It needs no parameter
                   and returns an integer.
"""


class Queue(object):
    """Implementation of queue data structure"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []