# Uses python3

from sys import stdin


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


def explore_reversed_graph(init_v):
    stack = list()
    stack.append(init_v)

    while stack:
        v = stack[-1]
        is_pushed = False
        for adj_v in reverse_adjacent_list[v]:
            if not pre_time[adj_v]:
                global pre_time_cnt
                pre_time_cnt += 1
                pre_time[adj_v] = pre_time_cnt

                stack.append(adj_v)
                is_pushed = True
                break

        if not is_pushed:
            complete_v = stack.pop(-1)
            global post_time_cnt
            post_time_cnt += 1
            post_time[complete_v] = (complete_v, post_time_cnt)


def explore(init_v):
    visited[init_v] = True

    stack = list()
    stack.append(init_v)

    while stack:
        v = stack[-1]
        is_pushed = False

        for adj_v in adjacent_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = True
                stack.append(adj_v)
                is_pushed = True
                break

        if not is_pushed:
            stack.pop(-1)


def test(num):
    global n, m, adjacent_list, reverse_adjacent_list, post_time, post_time_cnt, visited, pre_time, pre_time_cnt

    with open('tests/{}'.format(num)) as input_:
        n, m = list(map(int, input_.readline().split(' ')))

        adjacent_list = [list() for _ in range(n)]
        reverse_adjacent_list = [list() for _ in range(n)]

        for _ in range(m):
            v1, v2 = list(map(int, input_.readline().split(' ')))
            adjacent_list[v1 - 1].append(v2 - 1)
            reverse_adjacent_list[v2 - 1].append(v1 - 1)

        pre_time = [None for _ in range(n)]
        post_time = [None for _ in range(n)]
        pre_time_cnt = 0
        post_time_cnt = 0

        visited = [False for _ in range(n)]

        result = number_of_strongly_connected_components()

    with open('tests/{}.a'.format(num)) as output:
        expected_result = int(output.readline().strip('\n'))

        assert result == expected_result


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))

    adjacent_list = [list() for _ in range(n)]
    reverse_adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1-1].append(v2 - 1)
        reverse_adjacent_list[v2-1].append(v1 - 1)

    pre_time = [None for _ in range(n)]
    pre_time_cnt = 0
    post_time = [None for _ in range(n)]
    post_time_cnt = 0

    visited = [False for _ in range(n)]

    print(number_of_strongly_connected_components())
    # test(1)
    # test(2)
    # test(3)
