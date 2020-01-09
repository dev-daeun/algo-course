#Uses python3
from sys import stdin


# Time Complexity: O(|V| + |E|)
# while문은 정점의 갯수만큼 실행된다.
# 정점 1개에 의해 while문 1번이 돌 때, while문 안의 for문은 그 정점이 가진 간선의 갯수만큼 실행된다.
# (그래프 2개를 직접 그리면서 세어보면 알 수 있음.)

# Memory Complexity: O(|E|)
# adjacent_list는 각 정점이 가진 간선에 대한 정보를 저장하므로 간선의 갯수에 의해 공간복잡도가 결정된다.
def distance(n, adjacent_list, start, end):
    queue = list()
    queue.append(start)
    visited[start] = True
    dist = [-1 for _ in range(n)]
    dist[start] = 0

    while queue:
        v = queue.pop(0)
        if v == end:
            return dist[end]
        for adj_v in adjacent_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = True
                dist[adj_v] = dist[v] + 1
                queue.append(adj_v)
    return -1


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    adjacent_list = [list() for _ in range(n)]
    for _ in range(m):
        v1, v2 = list(map(int, stdin.readline().split()))
        adjacent_list[v1-1].append(v2 - 1)
        adjacent_list[v2-1].append(v1 - 1)
    
    visited = [False for _ in range(n)]
    start, end = list(map(int, stdin.readline().split()))
    print(distance(n, adjacent_list, start-1 , end-1))
