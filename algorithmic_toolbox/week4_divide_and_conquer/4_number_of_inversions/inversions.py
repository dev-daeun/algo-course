# Uses python3
import sys


def small_input():
    input_data = [2, 3, 9, 2, 9]
    expected_result = 2  # (3, 2), (9, 2)
    return input_data, expected_result


# Time Complexity : O(nlogn)
def get_number_of_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    merged_left, count_left = get_number_of_inversions(a[:mid])
    merged_right, count_right = get_number_of_inversions(a[mid:])
    merged, count_ = merge(merged_left, merged_right)
    return merged, count_left + count_right + count_


def merge(left, right):
    merged_result = []
    count_inversion = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]: 
            count_inversion += len(left) - i
            merged_result.append(right[j])
            j += 1
        else:
            merged_result.append(left[i])
            i += 1
    if i == len(left):
        merged_result.extend(right[j:])
    if j == len(right):
        merged_result.extend(left[i:])
    return merged_result, count_inversion


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    sorted_result, count_inversion = get_number_of_inversions(a)
    print(count_inversion)
