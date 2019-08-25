# python3


MAX_VALUE = pow(10, 9)
MIN_VALUE = -1


class MinHeap(object):
    def __init__(self, data):
        self.data = data
        self.result = []

    @property
    def size(self):
        return len(self.data)

    @staticmethod
    def left_idx(i):
        return 2 * i

    @staticmethod
    def right_idx(i):
        return 2 * i + 1

    def left(self, i):
        try:
            return self.data[self.left_idx(i)]
        except IndexError:
            return MAX_VALUE + 1

    def right(self, i):
        try:
            return self.data[self.right_idx(i)]
        except IndexError:
            return MAX_VALUE + 1

    def sift_down(self, i):
        parent = i
        while True:
            left = self.left(parent)
            right = self.right(parent)
            smallest = min(self.data[parent], left, right)

            if smallest == left:
                left_idx = self.left_idx(parent)
                self.data[parent], self.data[left_idx] = self.data[left_idx], self.data[parent]
                self.result.append(f'{parent} {left_idx}')
                parent = left_idx

            if smallest == right:
                right_idx = self.right_idx(parent)
                self.data[parent], self.data[right_idx] = self.data[right_idx], self.data[parent]
                self.result.append(f'{parent} {right_idx}')
                parent = right_idx

            if smallest == self.data[parent]:
                break

    def build_heap(self):
        mid = (self.size - 1) // 2
        for x in range(mid, 0, -1):
            self.sift_down(x)
        return self.result


def main_for_test():
    n, elements = open('./tests/04').read().splitlines()
    elements = list(map(int, elements.split()))

    m, *swaps = open('./tests/04.a').read().splitlines()

    min_heap = MinHeap(data=elements)
    result = min_heap.build_heap()

    print(len(result))
    assert len(result) == m
    assert result == swaps
    '''
    form of result : ['i0 j0', 'i1 j0', ...]
    '''


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main_for_test()
