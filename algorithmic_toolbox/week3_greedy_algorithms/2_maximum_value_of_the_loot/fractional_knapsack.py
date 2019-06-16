# Uses python3
import sys


# time complexity of sorted(): O(nlogn)
# time complexity of while loop: O(n)
# -> O(nlogn + n) = O(nlogn)
def get_optimal_value(capacity, weights, values):
    v_per_w = [{'unit_val': v / w,  'weight': w} for v, w in zip(values, weights)]
    sorted_v_per_w = sorted(v_per_w, key=lambda dic: dic['unit_val'], reverse=True)
    total_value = 0
    i = 0
    while capacity > 0 and i <= len(sorted_v_per_w) - 1:
        if capacity >= sorted_v_per_w[i]['weight']:
            total_value += sorted_v_per_w[i]['weight'] * sorted_v_per_w[i]['unit_val']
            capacity -= sorted_v_per_w[i]['weight']
        else:
            total_value += capacity * sorted_v_per_w[i]['unit_val']
            capacity = 0
        i += 1
    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
