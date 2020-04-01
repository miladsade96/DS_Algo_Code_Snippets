"""
    Dynamic Array Implementation
"""

# import relevant libraries
import ctypes


class DynamicArray(object):
    """Implementation of a dynamic array"""
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
