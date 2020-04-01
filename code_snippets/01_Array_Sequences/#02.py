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

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError("item is out of bounds!")
        else:
            return self.A[item]

    def append(self, item):
        if self.n == self.capacity:
            # 2x if capacity is not enough
            self._resize(2 * self.capacity)
        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    @staticmethod
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


def main():
    pass