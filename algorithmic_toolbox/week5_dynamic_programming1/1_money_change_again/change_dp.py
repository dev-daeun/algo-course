# Uses python3
import sys


def small_test():
    input_data = 34
    answer = 9  # 34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
    return input_data, answer


def big_test():
    input_data = 1003
    answer = 251  # 1000 = 4 * 250 + 3 * 1
    return input_data, answer


def edge_test():
    input_data = 1
    answer = 1
    return input_data, answer


# Time Complexity : O(m)
def get_change(m):
    answers = [0]
    for idx in range(1, m+1):
        try:
            min_coins_4 = answers[idx-4]
        except IndexError:
            min_coins_4 = 1001
        
        try:
            min_coins_3 = answers[idx-3]
        except IndexError:
            min_coins_3 = 1001
        
        min_coins_1 = answers[idx-1]
        m_answer = min(min_coins_1, min_coins_3, min_coins_4) + 1
        answers.append(m_answer)
    return answers[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # m, expected_answer = small_test()
    # answer = get_change(m)
    # print(answer)
    # assert answer == expected_answer

    # m, expected_answer = big_test()
    # answer = get_change(m)
    # assert answer == expected_answer

    # m, expected_answer = edge_test()
    # answer = get_change(m)
    # assert answer == expected_answer


