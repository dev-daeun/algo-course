def small_test1():
    input_data = 'ab', 'ab'
    result = 0
    return input_data, result


def small_test2():
    input_data = 'short', 'ports'
    result = 3
    return input_data, result


def small_test3():
    input_data = 'editing', 'distance'
    result = 5
    return input_data, result


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print('----------------')


# Time Complexity: O(length of s * length of t)
def edit_distance(s, t):
    s = '0' + s
    t = '0' + t
    matrix = []
    s_len = len(s)
    t_len = len(t)
    for _ in range(s_len):
        matrix.append([0] * t_len)

    for i in range(1, s_len):
        matrix[i][0] = i

    for j in range(1, t_len):
        matrix[0][j] = j

    for i in range(1, s_len):
        for j in range(1, t_len):
            insertion = matrix[i][j-1] + 1
            deletion = matrix[i-1][j] + 1
            mismatch = matrix[i-1][j-1] + 1
            match = matrix[i-1][j-1]

            if s[i] == t[j]:
                matrix[i][j] = min(insertion, deletion, match)
            else:
                matrix[i][j] = min(insertion, deletion, mismatch)

    return matrix[s_len-1][t_len-1]


if __name__ == "__main__":
    inputs, expected = small_test1()
    result = edit_distance(inputs[0], inputs[1])
    print(result)
    assert result == expected

    inputs, expected = small_test2()
    result = edit_distance(inputs[0], inputs[1])
    print(result)
    assert result == expected

    inputs, expected = small_test3()
    result = edit_distance(inputs[0], inputs[1])
    print(result)
    assert result == expected
