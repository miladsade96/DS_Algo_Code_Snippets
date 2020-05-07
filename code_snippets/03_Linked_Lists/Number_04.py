"""
    Linked List Reversal

    Problem:
        write a function reverse a linked list in place. The function
        will take in a head of the list as input and return the new
        head of the list.

    Solution:
        Since we want to do this in place,  we want to make the function
        operate in O(1) space, meaning we don't' want to create a new List
        , so we will simply use the current nodes. Time wise, we can perform
        the reversal in O(n) time.

        We can reverse the list by changing the next pointer of each node.
        Each node's next pointer should point to the previous node. In one
        pass head to tail of our input list, we will point each node's next
        pointer to the previous element.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"Node({self.value})"


def reverse(head: Node) -> Node:
    """
    This function reverses the linked list
    :param head: first node of the linked list
    :return: The first node of the reversed linked list
    """
    current = head
    previous = None
    nextNode = None
    while current:
        nextNode = current.next_node
        current.next_node = previous
        previous = current
        current = nextNode
    return previous
