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

    @property
    def empty(self):
        return not bool(self.tail)

    def push(self, node):
        if self.tail:
            self.tail.next_ = node
            node.prev_ = self.tail
        self.tail = node

    def pop(self):
        if self.tail:
            prev = self.tail.prev_
            prev.next_ = None
            self.tail.prev_ = None
            self.tail = prev
            return None
        raise Exception()
    
    def max(self):
        pass


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert(0)
