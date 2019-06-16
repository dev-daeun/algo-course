# Uses python3
import sys

COINS = [10, 5, 1]


# time complexity: O(n)
def get_change(m):
    total = 0
    for coin in COINS:
        share = m // coin
        rest = m % coin

        if share >= 1:
            total += share
            m = rest

    return total


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
