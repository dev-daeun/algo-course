# Uses python3

from sys import stdin, maxsize


class Vertex:
    def __init__(self, number):
        self.number = number
        self.dist = maxsize


def relax(v, adj_v, weight, vertices):
    if vertices[v].dist + weight < vertices[adj_v].dist:
        vertices[adj_v].dist = vertices[v].dist + weight


# Time complexity:
#  |V| * (sorted() 시간복잡도 + |E|/|V|) = O(|V| * sorted() 시간복잡도 + |E|)
def dijkstra(n, adjacent_list, start, end):
    vertices = [Vertex(i) for i in range(n)]
    vertices[start].dist = 0

    q = list()
    for i in range(n):
        q.append(vertices[i])

    # PriorityQueue는 Vertex 객체의 dist가 변경되어도 큐 내부에서 객체 간의 순서가 바뀌지 않아서 사용하기 부적절함.
    while q:
        q = sorted(q, key=lambda x: x.dist)
        v = q.pop(0)
        if v.number == end:
            return v.dist
        for adj_v, w in adjacent_list[v.number]:
            relax(v.number, adj_v, w, vertices)

    return -1


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    adjacent_list = [list() for _ in range(n)]

    for _ in range(m):
        v1, v2, weight = list(map(int, stdin.readline().split()))
        adjacent_list[v1-1].append((v2 - 1, weight))

    start, end = list(map(int, stdin.readline().split()))

    result = dijkstra(n, adjacent_list, start - 1, end - 1)
    if result == maxsize:
        print(-1)
    else:
        print(result)
