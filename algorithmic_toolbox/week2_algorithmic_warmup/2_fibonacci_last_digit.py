# Uses python3
import sys

LAST_DIGIT_CYCLE = 60


def get_fibonacci_last_digit_naive(n):
    pre = 1
    cur = 1
    last_digits = [1, 1]
    for _ in range(LAST_DIGIT_CYCLE - 2):
        pre, cur = cur, pre + cur
        last_digits.append(cur % 10)

    if n <= 0:
        return n
    if n <= 60:
        return last_digits[n-1]
    else:
        return last_digits[(n % LAST_DIGIT_CYCLE) - 1]
    

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
