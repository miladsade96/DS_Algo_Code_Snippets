"""
    Binary Heap Implementation

    Operations:
        1. BinaryHeap(): Creates a new, empty binary tree.
        2. insert(k): Adds a new item to the heap.
        3. find_min(): Returns the item with the minimum key value,
            leaving item in the heap.
        4. del_min(): Returns the item with the minimum key value,
            removing the item from the heap.
        5. is_empty(): Returns true if the heap is empty, false otherwise.
        6. size(): Returns the number of the items in the heap.
        7. build_heap(list): Builds a new heap from a list of keys.
"""


class BinaryHeap(object):
    """ Implementation of the Binary Heap"""

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.current_size]
        self.current_size = self.current_size - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
