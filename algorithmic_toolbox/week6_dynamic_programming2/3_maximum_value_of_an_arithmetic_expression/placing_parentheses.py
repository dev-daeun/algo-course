# Uses python3
import pprint
import sys


pp = pprint.PrettyPrinter(indent=2)


def evalt(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(expression):
    amount_of_digits = len(expression) // 2 + 1
    min_arr = [[0] * amount_of_digits for _ in range(amount_of_digits)]
    max_arr = [[0] * amount_of_digits for _ in range(amount_of_digits)]

    # 0-index based in expression list.
    # max, min value of each single digit is its value.
    for i in range(amount_of_digits):
        min_arr[i][i] = int(expression[2*i])
        max_arr[i][i] = int(expression[2*i])
    
    # diff : difference between j and i. 
    # Bigger the k, Longer the length of sub-expression.
    for diff in range(1, amount_of_digits):
        for start in range(0, amount_of_digits - diff):

            end = start + diff
            min_val = sys.maxsize
            max_val = -sys.maxsize - 1
            for sep in range(start, end):
                op = expression[2*sep+1]
                a = evalt(min_arr[start][sep], op, min_arr[sep+1][end])
                b = evalt(min_arr[start][sep], op, max_arr[sep+1][end])
                c = evalt(max_arr[start][sep], op, max_arr[sep+1][end])
                d = evalt(max_arr[start][sep], op, min_arr[sep+1][end])
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            
            min_arr[start][end] = min_val
            max_arr[start][end] = max_val

    return max_arr[0][amount_of_digits-1]

def test1():
    result = get_maximum_value('1+5')
    print(result)
    assert result == 6


def test2():
    result = get_maximum_value('5-8+7*4-8+9')
    print(result)
    assert result == 200

def test3():
    result = get_maximum_value('1+2-3*4-5')
    print(result)
    assert result == 6

if __name__ == "__main__":
    print(get_maximum_value(input()))
    # test1()
    # test2()
    # test3()
