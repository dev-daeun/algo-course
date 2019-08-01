# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev_ = None
        self.next_ = None


class DoubleLinkedList(object):
    def __init__(self):
        self.tail = None

    @property
    def empty(self):
        return not bool(self.tail)

    def add_at_tail(self, node):
        if self.tail:
            self.tail.next_ = node
            node.prev_ = self.tail
        self.tail = node

    def pop_tail(self):
        if self.tail:
            prev = self.tail.prev_
            prev.next_ = None
            self.tail.prev_ = None
            del self.tail
            self.tail = prev
        
        
if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
