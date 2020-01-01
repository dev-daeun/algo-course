# Uses python3

import sys


def dfs(v):
    visited[v] = True
    for adj_v in adjacent_list[v]:
        if not visited[adj_v]:
            dfs(adj_v)


# Time complexity: O(|V| + |E|)
def count_connected_component(n):
    cnt = 0

    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)

    return cnt


n, m = list(map(int, sys.stdin.readline().strip('\n').split()))
visited = [False for _ in range(n)]

adjacent_list = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = list(map(int, sys.stdin.readline().strip('\n').split()))
    adjacent_list[v1-1].append(v2 - 1)
    adjacent_list[v2-1].append(v1 - 1)

print(count_connected_component(n))


# ------------- test -------------
def test_input(num):
    with open('tests/{}'.format(num)) as inputs:
        n, m = list(map(int, inputs.readline().strip('\n').split()))
        global visited
        visited = [False for _ in range(n)]

        global adjacent_list
        adjacent_list = [[] for _ in range(n)]
        for _ in range(m):
            v1, v2 = list(map(int, inputs.readline().strip('\n').split()))
            adjacent_list[v1 - 1].append(v2 - 1)
            adjacent_list[v2 - 1].append(v1 - 1)

        result = count_connected_component(n)

    with open('tests/{}.a'.format(num)) as outputs:
        expected_result = int(outputs.readline().strip('\n'))

    assert result == expected_result


# test_input(1)
