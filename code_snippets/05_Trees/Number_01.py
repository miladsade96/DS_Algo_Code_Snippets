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

    def insert_left(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild
