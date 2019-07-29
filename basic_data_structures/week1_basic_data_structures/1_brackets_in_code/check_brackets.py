# python3
from array import array
from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    return_val_if_fail = None
    for i, val in enumerate(text):
        if val not in '()[]{}':
            continue
        if not stack:
            return_val_if_fail = i + 1
            stack.append(val)
            continue
        top = stack[-1]
        if are_matching(top, val):
            stack.pop()
        else:
            stack.append(val)
    if not stack:
        return 'Success'
    return return_val_if_fail


def main():
    # text = input()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = cur_dir + '/tests/'
    for num in range(1, 55):
        if num < 10:
            num = f'0{num}'
        input_ = open(test_dir + f'{num}').read()
        output_ = open(test_dir + f'{num}.a').read().strip('\n')
        result = find_mismatch(input_)
        print(f'num: {num}')
        print(f'result: {result}')
        print(f'output: {output_}')
        assert str(result) == output_
    # mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
