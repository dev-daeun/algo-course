# Uses python3
from math import pow
from sys import stdin


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DisjointSet:
    def __init__(self, vertexes, n):
        self.parents = list(range(n))
        self.vertexes = vertexes
        self.ranks = [0 for _ in range(n)]

    def find(self, e):
        p = e
        while self.parents[p] != p:
            p = self.parents[p]
        self.parents[e] = p
        return p

    def merge(self, dst, src):
        self.parents[src] = dst

    def union(self, v1, v2):
        v1_root = self.find(v1)
        v2_root = self.find(v2)

        if self.ranks[v1_root] == self.ranks[v2_root]:
            self.ranks[v1_root] += 1
            return self.merge(dst=v1_root, src=v2_root)

        if self.ranks[v1_root] > self.ranks[v2_root]:
            return self.merge(dst=v1_root, src=v2_root)

        return self.merge(dst=v2_root, src=v1_root)


def distance(city1, city2):
    return pow(pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2), 0.5)


def kruskal(n, vertexes, dist):
    sorted_dist = sorted(dist, key=lambda e: e[2])
    disjoint_set = DisjointSet(vertexes, n)
    sum_of_edges = 0.

    for v1, v2, d in sorted_dist:
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            disjoint_set.union(v1, v2)
            sum_of_edges += d

    return sum_of_edges


if __name__ == '__main__':
    number_of_v = int(stdin.readline().strip('\n'))
    vertexes = list()
    dist = list()

    for _ in range(number_of_v):
        x, y = list(map(int, stdin.readline().split(' ')))
        v = City(x, y)

        for idx, prev_v in enumerate(vertexes):
            dist.append((idx, len(vertexes), distance(prev_v, v)))

        vertexes.append(v)

    print("{0:.9f}".format(kruskal(number_of_v, vertexes, dist)))
