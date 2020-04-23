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
    def __repr__(self):
        return f"Node({self.value})"


def main():
    # Building Our Nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)

    # Building linked list using nodes
    a.next_node = b
    b.next_node = c

    # Testing linked list
    # Testing value attribute
    print(f"a.value -> {a.value}")
    print(f"b.value -> {b.value}")
    print(f"c.value -> {c.value}")
    # Testing next_node attribute
    print(f"a.next_node --> {a.next_node}")
    print(f"b.next_node --> {b.next_node}")
    print(f"c.next_node --> {c.next_node}")


if __name__ == '__main__':
    main()
