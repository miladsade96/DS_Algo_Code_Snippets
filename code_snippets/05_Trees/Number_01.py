"""
    Representing a Tree
    Nodes and References
"""


class BinaryTree(object):
    """Implementation of binary tree using nodes and references"""
    def __init__(self, rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild = None
