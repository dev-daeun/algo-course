# Uses python3
import sys


# time complexity: O(logN)
def gcd(a, b):
    num, share = (a, b) if a > b else (b, a) 
    remainder = num % share
    if remainder != 0:
        return gcd(share, remainder)
    else:
        return share


def lcm(a, b):
    return (a * b) // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))