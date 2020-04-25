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


if __name__ == '__main__':
    main()
