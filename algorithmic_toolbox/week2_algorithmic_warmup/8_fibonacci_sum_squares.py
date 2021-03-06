# Uses python3
LAST_DIGIT_CYCLE = 60


def get_fibo_sum_of_sqaure(n):
    if n <= 1:
        return n


    pre = 0
    cur = 1
    sum_ = 1  
    for _ in range(1, n):
        pre, cur = cur, pre + cur
        sum_ += cur * cur
    return sum_


# time complexity: O(1)
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
