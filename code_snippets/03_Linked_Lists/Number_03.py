"""
    Singly linked list cycle check

    Problem:
        Given a singly linked list, write a function which takes in the
        first node in a singly linked list and returns a boolean indicating
        if the linked list contains a cycle.
        A cycle is when a node's next point actually points back to a previous
        node in the list.

    Solution:
        To solve this problem we will have two markers traversing through the list.
        marker_1 and marker_2. We will have both markers begin at the first node of
        the list and traverse through the linked list. However the second marker,
        marker_2, will move two nodes ahead from every one node that marker_1 moves.
"""

from .Number_01 import Node


def cycle_check(node: Node) -> bool:
    """
    Implementation of the algorithm(solution)
    :param node: Given Node object that we want to check
    :return: Either True or False
    """
    # defining markers
    marker_1 = node
    marker_2 = node
    while marker_2 is not None and marker_2.next_node is not None:
        marker_1 = marker_1.next_node
        marker_2 = marker_2.next_node.next_node
        if marker_2 == marker_1:
            return True
    return False
