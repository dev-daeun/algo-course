# Uses python3

from sys import stdin, setrecursionlimit


setrecursionlimit(200000)


def number_of_strongly_connected_components():
    tag = 0
    sorted_reversed_graph = topological_sort_reverse()
    for v in sorted_reversed_graph:
        if not visited[v]:
            explore(v)
            tag += 1
    return tag


def topological_sort_reverse():
    for i in range(n):
        if not post_time[i]:
            explore_reversed_graph(i)

    sorted_result = sorted(post_time, key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_result]


def explore_reversed_graph(v):
    for adj_v in reverse_adjacent_list[v]:
        if not post_time[adj_v]:
            explore_reversed_graph(adj_v)

    global post_time_cnt
    post_time_cnt += 1
    post_time[v] = (v, post_time_cnt)


def explore(v):
    visited[v] = True
    for adj_v in adjacent_list[v]:
        if not visited[adj_v]:
            explore(adj_v)


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))

    adjacent_list = [list() for _ in range(n)]
    reverse_adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1-1].append(v2 - 1)
        reverse_adjacent_list[v2-1].append(v1 - 1)

    post_time = [None for _ in range(n)]
    post_time_cnt = 0

    visited = [False for _ in range(n)]

    print(number_of_strongly_connected_components())
