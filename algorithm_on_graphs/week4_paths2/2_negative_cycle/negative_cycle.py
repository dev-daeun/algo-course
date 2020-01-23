# Uses python3

from sys import stdin


def relax(v, adj_v, w, dist):
    if dist[adj_v] > dist[v] + w:
        dist[adj_v] = dist[v] + w
        return True
    return False


# 그래프 내 negative cycle의 유무를 찾는 문제
# Time Complexity: O(|V| * |E|)
def is_negative_cycle(n, edges):
    dist = [-1 for _ in range(n)]

    for _ in range(n-1):  # O(|V|)
        for v1, v2, w in edges:  # O(|E|)
            relax(v1, v2, w, dist)

    for v1, v2, w in edges:  # O(|E|)
        if relax(v1, v2, w, dist):
            return 1
    return 0


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    edges = []
    for _ in range(m):
        v1, v2, w = list(map(int, stdin.readline().split()))
        edges.append((v1 - 1, v2 - 1, w))

    print(is_negative_cycle(n, edges))
