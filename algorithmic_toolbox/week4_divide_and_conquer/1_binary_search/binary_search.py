# Uses python3


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
small_answer = []
for x in SMALL_NUMBERS_TO_SEARCH:
    element = binary_search(SMALL_SORTED_ARRAY, x)
    small_answer.append(element)

assert SMALL_EXPECTED == small_answer

BIG_SORTED_ARRAY = [n for n in range(1, 10000)]
BIG_NUMBERS_TO_SEARCH = [m for m in range(1, 100)]
BIG_EXPECTED = [e for e in range(99)]
big_answer = []
for x in BIG_NUMBERS_TO_SEARCH:
    element = binary_search(BIG_SORTED_ARRAY, x)
    big_answer.append(element)

assert BIG_EXPECTED == big_answer
