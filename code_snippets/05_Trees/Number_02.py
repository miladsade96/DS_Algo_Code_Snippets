"""
    Tree Traversals:
        1. Preorder: We visit the first node first, thn recursively do
            a preorder traversal of the left subtree, followed by a
            recursive preorder traversal of the right subtree.
        2. Inorder: We recursively do an inorder traversal on the left
            subtree, visit the root node and finally do a recursive
            inorder traversal of the right subtree.
        3. Postorder: We recursively do a postorder traversal of the left
            subtree and the right subtree followed by a visit to the root
            node.
"""
# import relevant classes
from .Number_01 import BinaryTree


def preorder(tree: BinaryTree) -> None:
    """
    Preorder recursive implementation
    :param tree: passed binary tree object
    :return: None
    """
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree: BinaryTree) -> None:
    """
    Postorder recursive implementation
    :param tree: passed binary tree object
    :return: None
    """
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())
