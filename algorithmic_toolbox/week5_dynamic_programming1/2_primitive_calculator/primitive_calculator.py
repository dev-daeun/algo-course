# Uses python3
MAX_VALUE = pow(10, 6)


'''
Time Complexity: O(n)

Solution :
    1. Define 'k' as number between 2 and n. Initialize 'k' to 2.
    
    2. Find the shortest sequence among 'divide_3_seq', 'divide_2_seq', and 'minus_1_seq' which are defined as below:
          * divide_3_seq: optimal sequence of k / 3, which equals to 'sequence[k/2]'.
          * divide_2_seq: optimal sequence of k / 2, which equals to 'sequence[k/3]'.
          * minus_1_seq: optimal sequence of k - 1, which equals to 'sequence[k-1]'.
          
       If k cannot be divided by 2 or 3, each length of sequence[k/2] and sequence[k/3] are transformed to MAX_VALUE.
       
    3. Memorize sequence of k as (the shortest sequence from above + k) and sequence of k becomes optimal.
    
    4. Iterate until k equals n.
'''


def optimal_sequence(n):
    sequence = [None, [1]]

    for k in range(2, n+1):
        sequence.append([])
        try:
            divide_3_seq = sequence[k//3]
            divide_3_seq_len = len(divide_3_seq) if k % 3 == 0 else MAX_VALUE
        except IndexError:
            divide_3_seq_len = MAX_VALUE
        try:
            divide_2_seq = sequence[k // 2]
            divide_2_seq_len = len(divide_2_seq) if k % 2 == 0 else MAX_VALUE
        except IndexError:
            divide_2_seq_len = MAX_VALUE

        plus_1_seq = sequence[k-1]
        plus_1_seq_len = len(plus_1_seq)
        optimal_sequence_len = min(divide_2_seq_len, divide_3_seq_len, plus_1_seq_len)

        if optimal_sequence_len == divide_3_seq_len:
            sequence[k].extend(divide_3_seq)
        elif optimal_sequence_len == divide_2_seq_len:
            sequence[k].extend(divide_2_seq)
        else:
            sequence[k].extend(plus_1_seq)
        sequence[k].append(k)
    return sequence[n]


def edge_test():
    input_ = 1
    k = 0
    seq = [1]
    return input_, k, seq


def small_test():
    input_ = 5
    k = 3
    seq = [1, 2, 4, 5]
    return input_, k, seq


def big_test():
    input_ = 96234
    k = 14
    seq = [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
    return input_, k, seq


edge_input, edge_k, edge_seq = edge_test()
edge_result = optimal_sequence(edge_input)
assert edge_k == len(edge_result) - 1
assert edge_seq == edge_result

small_input, small_k, small_seq = small_test()
small_result = optimal_sequence(small_input)
assert small_k == len(small_result) - 1
assert small_seq == small_result

big_input, big_k, big_seq = big_test()
big_result = optimal_sequence(big_input)
assert big_k == len(big_result) - 1
assert big_seq == big_result
