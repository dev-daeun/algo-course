# python3
import sys


# Safe Move:
# Choose the biggest profit from a.
# Choose the biggest click count from b.
# Multiply them.
# (the bigger the profit, the more it should be clicked.)

# time complexity: O(n)
def max_dot_product(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    total = 0

    for aa, bb in zip(sorted_a, sorted_b):
        total += aa * bb

    return total


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

