# Uses python3

import sys


# Time complexity: O(|E|)
def is_in_same_connected_component(start, end):
    if start == end:
        return 1

    visited[start] = True
    for adj_v in adjacent_list[start]:
        if not visited[adj_v]:
            result = is_in_same_connected_component(adj_v, end)
            if result:
                return result

    return 0


n, m = list(map(int, sys.stdin.readline().strip('\n').split()))
visited = [False for _ in range(n)]

adjacent_list = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = list(map(int, sys.stdin.readline().strip('\n').split()))
    adjacent_list[v1-1].append(v2 - 1)
    adjacent_list[v2-1].append(v1 - 1)

start, end = list(map(int, sys.stdin.readline().strip('\n').split()))
start -= 1
end -= 1

print(is_in_same_connected_component(start, end))


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

        start, end = list(map(int, inputs.readline().strip('\n').split()))
        start -= 1
        end -= 1

        result = is_in_same_connected_component(start, end)

    with open('tests/{}.a'.format(num)) as outputs:
        expected_result = int(outputs.readline().strip('\n'))

    assert result == expected_result

# test_input(1)
# test_input(2)
# test_input(3)
