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


'''
어떤 정점에서 인접한 다른 정점을 방문하려고 할 때, pre_time은 갱신되었으나 post_time이 갱신되어있지 않으면
두 정점은 사이클을 이루는 connected component에 있다.

DAG(Directed Acyclic Graph)의 경우, 이미 방문했으면서 인접한 정점은 pre_time, post_time 둘 다 갱신되어 있음.
'''


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


def test(num):
    global n
    global m
    global pre_time
    global post_time
    global adjacent_list

    with open('tests/{}'.format(num)) as input_:
        n, m = list(map(int, input_.readline().split(' ')))
        pre_time = [None for _ in range(n)]
        post_time = [None for _ in range(n)]
        adjacent_list = [list() for _ in range(n)]

        for _ in range(m):
            v1, v2 = list(map(int, input_.readline().split(' ')))
            adjacent_list[v1-1].append(v2 - 1)

        result = dfs()

    with open('tests/{}.a'.format(num)) as output:
        expected_result = int(output.readline())
        assert result == expected_result


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    pre_time = [None for _ in range(n)]
    post_time = [None for _ in range(n)]
    adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1-1].append(v2 - 1)

    print(1) if dfs() else print(0)

    # test(1)
    # test(2)
