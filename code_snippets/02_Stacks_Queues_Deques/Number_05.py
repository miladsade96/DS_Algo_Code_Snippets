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
    pass
