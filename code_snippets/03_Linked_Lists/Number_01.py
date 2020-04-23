"""
    Implementation of Singly Linked List

    Pros:
        (1) - Linked lists have constant time insertions and deletions
              in any position, in comparison, arrays require O(n) time
              to do the same thing.
        (2) - Linked lists can continue to expand without having to
              specify their size ahead of time.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
