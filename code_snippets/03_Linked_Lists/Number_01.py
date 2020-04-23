"""
    Implementation of Singly Linked List

    Pros:
        (1) - Linked lists have constant time insertions and deletions
              in any position, in comparison, arrays require O(n) time
              to do the same thing.
        (2) - Linked lists can continue to expand without having to
              specify their size ahead of time.

    Cons:
        (1) - To access an element in a linked list, you need to take
              O(k) to go from the head of the list to the k-th element.
              In contrast, arrays have constant time operations to access
              element in an array.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def main():
    pass


if __name__ == '__main__':
    main()
