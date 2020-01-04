# Uses python3
from time import time
from sys import stdin


def acyclic(adj):
    return 0


def dfs():
    for i in range(n):
        if not pre_time[i]:
            explore(i)


def explore(v):
    pre_time[v] = time()

    for adj_v in adjacent_list[v]:
        if not pre_time[adj_v]:
            explore(adj_v)

    post_time[v] = time()


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    pre_time = [None for _ in range(n)]
    post_time = [None for _ in range(n)]
    adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1-1].append(v2 - 1)

    dfs()

