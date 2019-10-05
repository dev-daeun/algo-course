#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def test1():
    input_ = (
        (2, 1, 2),
        (1, -1, -1),
        (3, -1, -1),
    )
    root = build_tree(input_)
    assert is_bst(root)


def test2():
    input_ = (
        (1, 1, 2),
        (2, -1, -1),
        (3, -1, -1),
    )

    root = build_tree(input_)
    assert not is_bst(root)


def test3():
    input_ = (
        (1, -1, 1),
        (2, -1, 2),
        (3, -1, 3),
        (4, -1, 4),
        (5, -1, -1),
    )

    root = build_tree(input_)
    assert is_bst(root)


def test4():
    input_ = (
        (4, 1, 2),
        (2, 3, 4),
        (6, 5, 6),
        (1, -1, -1),
        (3,  -1, -1),
        (5, -1, -1),
        (7, -1, -1)
    )

    root = build_tree(input_)
    assert is_bst(root)


def test5():
    input_ = (
        (4, 1, -1),
        (2, 2, 3),
        (1, -1, -1),
        (5, -1, -1),
    )

    root = build_tree(input_)
    assert not is_bst(root)


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = None if left == -1 else left
        self.right = None if right == -1 else right


def build_tree(relations):
    result = []
    for r in relations:
        key, left, right = r
        #  init node's left, right with children's indexes.(<int> type)
        v = Node(key, left, right)
        result.append(v)

    # replace children's index with children themselves(<Node> type).
    for node in result:
        try:
            node.left = result[node.left]
        except TypeError:
            node.left = None

        try:
            node.right = result[node.right]
        except TypeError:
            node.right = None

    return result[0]  # Vertex 0 is the root.


def is_leaf(root):
    return not root.left and not root.right


def is_bst(root):
    if not root:
        return True

    if not is_bst(root.left):
        return False

    if not is_bst(root.right):
        return False

    if root.left:
        if root.left.key > root.key:
            return False

    if root.right:
        if root.right.key < root.key:
            return False

    return True


def main():
    # nodes = int(sys.stdin.readline().strip())
    # tree = []
    # for i in range(nodes):
    #     tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # if is_bst(tree):
    #     print("CORRECT")
    # else:
    #     print("INCORRECT")
    # test1()
    # test2()
    # test3()
    # test4()
    test5()


threading.Thread(target=main).start()
