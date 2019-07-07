# Uses python3
import sys

def small_test():
    input_data = [2, 3, 9, 2, 2]
    expected_outout = 1
    return input_data, expected_outout


def big_test():
    input_data = list(range(10000))
    expected_output = 0
    return input_data, expected_output


# Time Complexity: O(n)
def get_majority_element(a):
    count_table = {}
    for num in a:
        count_table[num] = count_table.setdefault(num, 0) + 1

    half = len(a) // 2
    for _, val in count_table.items():
        if val > half:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    result = get_majority_element(a)
    print(result)