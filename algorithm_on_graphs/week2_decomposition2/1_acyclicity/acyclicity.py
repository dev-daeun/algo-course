# Uses python3
from time import time
from sys import stdin


def dfs():
    for i in range(n):
        if not pre_time[i]:
            result = is_cyclic(i)
            if result:
                return True
    return False


def is_cyclic(v):
    pre_time[v] = time()

    for adj_v in adjacent_list[v]:
        if pre_time[adj_v]:
            if not post_time[adj_v]:
                return True
        else:
            result = is_cyclic(adj_v)
            if result:
                return True

    post_time[v] = time()
    return False


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    pre_time = [None for _ in range(n)]
    post_time = [None for _ in range(n)]
    adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1-1].append(v2 - 1)

    print(1) if dfs() else print(0)

