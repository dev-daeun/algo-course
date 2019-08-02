# python3
import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev_ = None
        self.next_ = None


class StackWithMax(object):
    def __init__(self):
        self.tail = None
        self.max_ = None

    @property
    def empty(self):
        return not bool(self.tail)

    def iterate(self):
        p = self.tail
        while p:
            print(p.val, end=' ')
            p = p.prev_
        print()

    def push(self, node):
        if not self.empty:
            self.tail.next_ = node
            node.prev_ = self.tail
        self.tail = node
        self.refresh_max_after_push()

    def pop(self):
        if not self.empty:
            self.refresh_max_before_pop()
            prev = self.tail.prev_
            prev.next_ = None
            self.tail.prev_ = None
            self.tail = prev
            return None
        raise Exception()
    
    # Time Complexity: O(1)
    def refresh_max_after_push(self):
        if not self.max_:
            self.max_ = self.tail
            return None 
        if self.max_.val < self.tail.val:
            self.max_ = self.tail
        return None

    # Time Complexity: O(n)
    def refresh_max_before_pop(self):
        if not self.max_:
            return None
        if self.max_ is self.tail:
            p = self.tail.prev_
            self.max_ = Node(-1)
            while p:
                if self.max_.val < p.val:
                    self.max_ = p
                p = p.prev_

    @property
    def max_val(self):
        return self.max_.val


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
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(Node(int(query[1])))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max_val)
        else:
            assert(0)
    # test1(StackWithMax())
    # test2(StackWithMax())
    # test3(StackWithMax())
    # test4(StackWithMax())
