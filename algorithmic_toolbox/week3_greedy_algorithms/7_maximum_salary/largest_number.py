# Uses python3
import itertools
import operator
import sys


def small_input1():
    # expected result: 923932423
    return [23, 39, 92, 24, 3]


def small_input2():
    # expected result: 221
    return [21, 2]


def small_input3():
    # expected result: 99641
    return [9, 4, 6, 1, 9]


def big_input():
    # expected result:
    # 9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010
    with open('./big_input') as f:
        line = f.readline()
        nums = line.split()
        return [int(n) for n in nums]


def get_digit(num, i):
    str_num = str(num)
    return int(str_num[i % len(str_num)])


# time complexity: O(NlogN)
# Greedy Choice:
# 이 문제에서 탐욕적인 선택은 숫자의 크기과 무관하게 자릿수가 클수록 무조건 앞에 오게 하는 것이다.
# Safe Move:
# 각 숫자들의 i번째 자릿수를 비교했을 때 i번째 자릿수가 가장 큰 숫자를 앞에 둔다.
# i번째 자릿수가 동일할 경우, (i+1)번째 자릿수를 비교한다.
# 어떤 숫자의 자릿수가 i보다 작다면, 숫자의 첫번째 자릿수로 돌아가서 비교한다. 즉, 숫자의 자릿수를 순회한다(cycle).
def largest_number(a):
    digit_len = len(str(max(a)))
    cycled_digits = [itertools.cycle(str(num)) for num in a]
    digit_lists = [itertools.islice(gen, digit_len) for gen in cycled_digits]
    for list_ in digit_lists:
        digit_lists[digit_lists.index(list_)] = ''.join(list(list_))
    list_to_sort = list(zip(a, digit_lists))
    sorted_nums = sorted(list_to_sort, key=lambda pair: operator.itemgetter(*range(digit_len))(pair[1]), reverse=True)
    return int(''.join([str(pair[0]) for pair in sorted_nums]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
