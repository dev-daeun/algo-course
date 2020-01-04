# Uses python3

from sys import stdin


def topological_sort():
    for i in range(n):
        if not post_time[i]:
            explore(i)

    sorted_result = sorted(post_time, key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_result]


def explore(v):
    for adj_v in adjacent_list[v]:
        if not post_time[adj_v]:
            explore(adj_v)

    global post_time_cnt
    post_time_cnt += 1
    post_time[v] = (v + 1, post_time_cnt)


def test(num):
    global n
    global m
    global post_time
    global adjacent_list
    global post_time_cnt
    post_time_cnt = 0

    with open('tests/{}'.format(num)) as input_:
        n, m = list(map(int, input_.readline().split(' ')))
        post_time = [None for _ in range(n)]

        adjacent_list = [list() for _ in range(n)]
        for _ in range(m):
            v1, v2 = list(map(int, input_.readline().split(' ')))
            adjacent_list[v1 - 1].append(v2 - 1)

    with open('tests/{}.a'.format(num)) as output:
        expected_result = output.readline().strip('\n')
        result = ' '.join([str(e) for e in topological_sort()])
        assert result == expected_result


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    post_time = [None for _ in range(n)]
    post_time_cnt = 0

    adjacent_list = [list() for _ in range(n)]
    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split(' ')))
        adjacent_list[v1 - 1].append(v2 - 1)

    result = topological_sort()
    print(' '.join([str(e) for e in result]))

    test(1)
    test(2)
    test(3)
