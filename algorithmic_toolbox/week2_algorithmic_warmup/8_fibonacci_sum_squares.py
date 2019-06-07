# Uses python3
LAST_DIGIT_CYCLE = 60


def get_fibo_sum_of_sqaure(n):
    if n <= 1:
        return n

    # the values of F1 and F0 is determined already so that
    # the first value of sum_ should also be determined as f1 + f0.
    pre = 0
    cur = 1
    sum_ = 1  
    for _ in range(1, n):
        pre, cur = cur, pre + cur
        sum_ += cur * cur
    return sum_

def fibonacci_sum_of_square_last_digit(n):
    remainders = []
    for k in range(1, LAST_DIGIT_CYCLE + 1):
        remainders.append(get_fibo_sum_of_sqaure(k) % 10)
    
    if n <= 0:
        return n
    if n <= 60:
        return remainders[n-1]
    else:
        return remainders[(n % LAST_DIGIT_CYCLE) - 1]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_of_square_last_digit(n))
