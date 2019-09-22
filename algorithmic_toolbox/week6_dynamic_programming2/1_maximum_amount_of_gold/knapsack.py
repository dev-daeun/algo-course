# Uses python3
import array
import pprint
import sys

pp = pprint.PrettyPrinter(indent=2)


def optimal_weight(W, n, golds):
    value = [array.array('L', [0] * (W + 1)) for _ in range(n+1)]
    golds.insert(0, None)  # 1-index based

    for i in range(1, n+1):
        for w in range(1, W+1):
            value[i][w] = value[i-1][w]
            if golds[i] <= w:
                nominate = value[i-1][w-golds[i]] + golds[i]
                value[i][w] = max(value[i][w], nominate)
    return value[n][W]

def test1():
    W = 10
    n = 3
    golds = [1, 4, 8]
    result = optimal_weight(W, n, golds)
    assert result == 9


def test2():
    W = 10
    n = 10
    golds = [1] * 10
    result = optimal_weight(W, n, golds)
    assert result == 10


def test3():
    W = 10
    n = 10
    golds = [0] * 10
    result = optimal_weight(W, n, golds)
    assert result == 0
 

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, n, w))
    # test1()
    # test2()
    # test3()