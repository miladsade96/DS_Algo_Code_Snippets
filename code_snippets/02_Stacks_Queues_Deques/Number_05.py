"""
    Problem:
        Implement a queue data structure using two stacks.
        Given a stack class below, implement a queue class using two stacks.
        Use a python list data structure as your stack.

    solution:
        The key insight is that a stack reverses order. A sequence of elements pushed
        on a stack comes back in the reversed order when popped. Consequently, two
        stacks chained together will return elements in the same order, since reversed
        order reversed again is original order.

"""


class TwoStackQueue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, element):
        self.in_stack.append(element)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
