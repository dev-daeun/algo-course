#!/usr/bin/python3
import sys
import threading

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


def test6():
    data = (
        (2, 1, 2),
        (1, -1, -1),
        (2, -1, -1),
    )

    root = build_tree(data)
    assert is_bst(root)


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = None if left == -1 else left
        self.right = None if right == -1 else right


def build_tree(relations):
    result = []
    for r in relations:
        key, left, right = r
        v = Node(key, left, right)
        result.append(v)

    for r in result:
        try:
            r.left = result[r.left]
        except TypeError:
            r.left = None

        try:
            r.right = result[r.right]
        except TypeError:
            r.right = None

    return result[0]


def is_leaf(root):
    return not (root.left or root.right)


def find_biggest_in_left(root):
    start = root.left
    if not start:
        return root.key
    while start.right:
        start = start.right
    return start.key


def find_smallest_in_right(root):
    start = root.right
    if not start:
        return root.key
    while start.left:
        start = start.left
    return start.key


def is_bst(root):
    if is_leaf(root):
        return True

    if root.left:
        is_left_bst = is_bst(root.left)
        if not is_left_bst or find_biggest_in_left(root) >= root.key:
            return False

    if root.right:
        is_right_bst = is_bst(root.right)
        if not is_right_bst or find_smallest_in_right(root) < root.key:
            return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())

    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    root = build_tree(tree)
    if is_bst(root):
        print("CORRECT")
    else:
        print("INCORRECT")

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


threading.Thread(target=main).start()
