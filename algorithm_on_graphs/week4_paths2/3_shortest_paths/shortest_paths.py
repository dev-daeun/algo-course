# Uses python3

from sys import stdin, maxsize


def relax(v, adj_v, w, dist):
    if dist[adj_v] > dist[v] + w:
        dist[adj_v] = dist[v] + w
        return True
    return False


def bellman_ford(n, start, adjacent_list):
    dist = [maxsize for _ in range(n)]
    dist[start] = 0

    for _ in range(n-1):  # O(|V|)
        for edges in adjacent_list:
            for adj_v, w in edges:  # O(|E|)
                relax(adjacent_list.index(edges), adj_v, w, dist)

    q = list()
    for edges in adjacent_list:
        for adj_v, w in edges:
            if relax(adjacent_list.index(edges), adj_v, w, dist):
                q.append(adj_v)

    visited = [False for _ in range(n)]
    while q:
        v = q.pop(0)
        for adj_v, _ in adjacent_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = True
                dist[adj_v] = '-'
                q.append(adj_v)

    return dist


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    adjacent_list = [list() for _ in range(n)]
    for _ in range(m):
        v1, v2, w = list(map(int, stdin.readline().split()))
        adjacent_list[v1-1].append((v2 - 1, w))

    start = int(stdin.readline().strip('\n'))
    dist = bellman_ford(n, start - 1, adjacent_list)
    for d in dist:
        print('*' if d == maxsize else d)
