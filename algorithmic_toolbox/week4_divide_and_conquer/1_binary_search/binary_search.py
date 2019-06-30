# Uses python3
import sys


def binary_search(array, target):
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


SMALL_SORTED_ARRAY = [1, 5, 8, 12, 13, 14]
SMALL_NUMBERS_TO_SEARCH = [8, 1, 23, 1, 11, 14]
SMALL_EXPECTED = [2, 0, -1, 0, -1, 5]

BIG_SORTED_ARRAY = [n for n in range(1, 10000)]
BIG_NUMBERS_TO_SEARCH = [m for m in range(1, 100)]
BIG_EXPECTED = [e for e in range(99)]


if __name__ == '__main__':
    input_ = sys.stdin.read()
    data = list(map(int, input_.split()))
    n = data[0]      # number of sorted array
    m = data[n+1]    # number of numbers to search
    sorted_array = data[1:n+1]  # sorted array
    numbers_to_search = data[n+2:]

    # n = len(SMALL_SORTED_ARRAY)
    # sorted_array = SMALL_SORTED_ARRAY
    # numbers_to_search = SMALL_NUMBERS_TO_SEARCH

    # n = len(BIG_SORTED_ARRAY)
    # sorted_array = BIG_SORTED_ARRAY
    # numbers_to_search = BIG_NUMBERS_TO_SEARCH

    answer = []
    for x in numbers_to_search:  # numbers to search
        element = binary_search(sorted_array, x)
        print(element, end=' ')
        answer.append(element)

    expected = SMALL_EXPECTED
    assert expected == answer
