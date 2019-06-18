# python3
import sys


# time complexity: O(n)
def compute_min_refills(distance, tank, stops):
    start = 0
    total = 0
    stops.insert(0, 0)
    stops.append(distance)
    dest = len(stops) - 1

    while True:
        if start == dest:
            break
        i = start + 1
        while i <= dest and stops[i] - stops[start] <= tank:  # find next station
            i += 1
        if i == start + 1:  # there is no station that can get with tank
            return -1
        if i - 1 < dest: # if next station is still not the destination
            total += 1
        start = i - 1 # set next station as start 
    return total

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
