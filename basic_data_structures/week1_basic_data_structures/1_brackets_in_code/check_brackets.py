# python3
from array import array
from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])

def match(left, right):
    return (left + right) in ["()", "[]", "{}"]

def empty(stack):
    return not bool(stack)

def prior_to_top(left, right):
    opening = '([{'
    closing = ')]}'

    if left in opening and right in closing:
        return False
    return True


def find_mismatch(text):
    stack = []
    result = None

    for i, val in enumerate(text):
        if val not in '()[]{}':
            continue

        if empty(stack):
            result = i
            stack.append(val)
            continue

        top = stack[-1]
        if match(top, val):
            stack.pop()
            if empty(stack):
                result = None
            continue

        if not prior_to_top(top, val):
            result = i
        stack.append(val)

    if result is not None:
        return result + 1
    else:
        return 'Success'

def main():
    # text = input()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = cur_dir + '/tests/'
    for num in range(1, 55):
        if num < 10:
            num = f'0{num}'
        input_ = open(test_dir + f'{num}').read().strip('\n')
        output_ = open(test_dir + f'{num}.a').read().strip('\n')

        print(f'------------- num: {num}')
        print(f'input: {input_}')
        result = find_mismatch(input_)
        print(f'expected: {output_}')
        print(f'result: {result}')
        assert str(result) == output_
    # mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
