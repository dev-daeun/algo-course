# Uses python3
def calc_fib(n):
    if n <= 0:
        return n
    if n <= 2:
        return 1
    pre = 1
    cur = 1
    for _ in range(n-1):
        cur, pre = pre, pre + cur
    return cur

n = int(input())
print(calc_fib(n))
