# Uses python3
import itertools
import operator
import sys


def small_input1():
    # expected result: 92 39 3 24 23
    return [23, 39, 92, 24, 3]


def small_input2():
    # expected result: 2 21
    return [21, 2]


def small_input3():
    # expected result: 9 9 6 4 1
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
def largest_number(a):
    digit_len = len(str(max(a)))
    cycled_digits = list(list(itertools.islice(itertools.cycle(str(num)), digit_len)) for num in a)
    for digit_list in cycled_digits:
        cycled_digits[cycled_digits.index(digit_list)] = ''.join(digit_list)
    list_to_sort = list(zip(a, cycled_digits))
    sorted_nums = sorted(list_to_sort, key=lambda pair: operator.itemgetter(*range(digit_len))(pair[1]), reverse=True)
    return int(''.join([str(pair[0]) for pair in sorted_nums]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
