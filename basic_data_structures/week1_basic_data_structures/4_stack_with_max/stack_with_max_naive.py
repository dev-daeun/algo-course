# python3
import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev_ = None
        self.next_ = None


class StackForTrackMax(object):
    def __init__(self):
        self.tail = None  # points current max 

    @property
    def empty(self):
        return not bool(self.tail)

    def push(self, node):
        new_node = Node(node.val)
        if self.empty:
            self.tail = new_node
            return None
        if self.tail.val <= new_node.val:
            self.tail.next_ = new_node
            new_node.prev_ = self.tail
            self.tail = new_node

    def pop(self, node):
        if self.tail.val == node.val:
            p = self.tail
            prev = self.tail.prev_
            if prev:
                prev.next_ = None
            self.tail.prev_ = None
            self.tail = prev
            return p
        return None


class StackWithMax(object):
    def __init__(self):
        self.tail = None
        self.max_tracker = StackForTrackMax()

    @property
    def empty(self):
        return not bool(self.tail)

    def push(self, node):
        if not self.empty:
            self.tail.next_ = node
            node.prev_ = self.tail
        self.tail = node
        self.max_tracker.push(node)

    def pop(self):
        if self.empty:
            return None
        p = self.tail
        prev = self.tail.prev_
        if prev:
            prev.next_ = None
        self.tail.prev_ = None
        self.tail = prev
        self.max_tracker.pop(p)
        return p

    @property
    def max_val(self):
        if self.max_tracker.tail:
            return self.max_tracker.tail.val
        return None


def test1(stack):
    stack.push(Node(2))
    stack.push(Node(1))
    m1 = stack.max_val
    stack.pop()
    m2 = stack.max_val

    assert m1 == 2
    assert m2 == 2


def test2(stack):
    stack.push(Node(1))
    stack.push(Node(2))
    m1 = stack.max_val
    stack.pop()
    m2 = stack.max_val

    assert m1 == 2
    assert m2 == 1

def test3(stack):
    stack.push(Node(2))
    stack.push(Node(3))
    stack.push(Node(9))
    stack.push(Node(7))
    stack.push(Node(2))

    assert stack.max_val == 9
    assert stack.max_val == 9
    assert stack.max_val == 9

    stack.pop()

    assert stack.max_val == 9


def test4(stack):
    stack.push(Node(7))
    stack.push(Node(1))
    stack.push(Node(7))
    assert stack.max_val == 7

    stack.pop()
    assert stack.max_val == 7

if __name__ == '__main__':
    # stack = StackWithMax()
    # num_queries = int(sys.stdin.readline())
    # for _ in range(num_queries):
    #     query = sys.stdin.readline().split()

    #     if query[0] == "push":
    #         stack.push(Node(int(query[1])))
    #     elif query[0] == "pop":
    #         stack.pop()
    #     elif query[0] == "max":
    #         print(stack.max_val)
    #     else:
    #         assert(0)
    test1(StackWithMax())
    test2(StackWithMax())
    test3(StackWithMax())
    test4(StackWithMax())
