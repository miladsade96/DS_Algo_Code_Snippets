"""
    Implementation of doubly linked list
"""


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
    def __repr__(self):
        return f"Node{self.value}"


def main():
    # Building our Nodes
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)

    # Building doubly linked list using nodes
    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b

    # Testing doubly linked list
    # Testing value attribute
    print(f"a.value --> {a.value}")
    print(f"b.value --> {b.value}")
    print(f"c.value --> {c.value}")


if __name__ == '__main__':
    main()
