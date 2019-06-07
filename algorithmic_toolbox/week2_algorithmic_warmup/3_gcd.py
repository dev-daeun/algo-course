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


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(a, b)
    print(gcd(a, b))