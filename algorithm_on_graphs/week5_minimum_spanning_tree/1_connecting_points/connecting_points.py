# Uses python3
from math import pow
from sys import stdin


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(city1, city2):
    return pow(pow(city1.x - city2.x, 2) + pow(city1.y - city2.y, 2), 0.5)


def minimum_distance(vertexes, edges):
    result = 0.
    # write your code here
    return result


if __name__ == '__main__':
    number_of_v = int(stdin.readline().strip('\n'))
    vertexes = list()
    edges = list()
    for _ in range(number_of_v):
        x, y = list(map(int, stdin.readline().split(' ')))
        v = City(x, y)

        for c in vertexes:
            edges.append((c, v, distance(c, v)))
        vertexes.append(v)

    sorted_edges = sorted(edges, key=lambda e: e[2])
    print("{0:.9f}".format(minimum_distance(vertexes, sorted_edges)))


