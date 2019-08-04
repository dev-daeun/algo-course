# python3

import os
import sys


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    @property
    def empty(self):
        return not bool(self.head)

    def enqueue(self, node):
        if not self.empty:
            self.tail.next_ = node
            node.prev_ = self.tail
        else:
            self.head = node
        self.tail = node

    def dequeue(self):
        if self.empty:
            return None
        p = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return p
        self.head.next_.prev_ = None
        self.head = self.head.next_
        p.next_ = None
        return p


class Node(object):
    def __init__(self, key, parent_key):
        self.key = key
        self.children = []
        self.parent_key = parent_key
        self.depth = None

        self.next_ = None
        self.prev_ = None


def compute_height(n, parents):
    arr = []

    # create each node and save it to list.
    for i, p in zip(range(n), parents):
        arr.append(Node(key=i, parent_key=p))

    # create a tree using the list.
    for i in range(n):
        if arr[i].parent_key == -1:
            arr[i].depth = 0
            root = arr[i]
        else:
            arr[arr[i].parent_key].children.append(arr[i])  

    q = Queue()
    q.enqueue(root)

    # breadth-first traversal
    while not q.empty:
        cur_node = q.dequeue()
        for child in cur_node.children:
            child.depth = cur_node.depth + 1
            q.enqueue(child)

    return cur_node.depth + 1


def main():
    # n = int(input())
    # parents = list(map(int, input().split()))
    # print(compute_height(n, parents))
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = cur_dir + '/tests/'
    for num in range(1, 25):
        if num < 10:
            num = f'0{num}'
        input_ = open(f'{test_dir}{num}').read().strip('\n')
        output_ = open(f'{test_dir}{num}.a').read().strip('\n')
        n, parents = input_.split('\n')
        
        print(f'----- test number {num} -----')
        result = compute_height(int(n), [int(p) for p in parents.split()])
        print(f'expected: {output_}')
        print(f'result: {result}')
        assert str(result) == output_

if __name__ == '__main__':
    main()