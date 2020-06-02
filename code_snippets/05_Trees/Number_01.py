"""
    Representing a Tree
    Nodes and References
"""
# importing relevant libraries
import unittest


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

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.r = BinaryTree("a")
        self.r.insert_left("b")
        self.r.insert_right("c")
        self.r.get_right_child().set_root_val("z")
