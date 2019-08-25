# python3


MAX_VALUE = pow(10, 9)


# 0-based indices of the elements to be swapped.
# left child's index: 2 * i + 1
# right child's index: 2 * i + 2
class MinHeap(object):
    def __init__(self, data):
        self.data = data
        self.result = []

    @property
    def size(self):
        return len(self.data)

    def left(self, i):
        try:
            return 2 * i + 1, self.data[2*i+1]
        except IndexError:
            return None, MAX_VALUE + 1

    def right(self, i):
        try:
            return 2 * i + 2, self.data[2*i+2]
        except IndexError:
            return None, MAX_VALUE + 1

    def is_leaf(self, i):
        left_idx, _ = self.left(i)
        right_idx, _ = self.right(i)

        return not (left_idx or right_idx)

    def sift_down(self, i):
        parent = i
        while not self.is_leaf(parent):
            left_idx, left = self.left(parent)
            right_idx, right = self.right(parent)
            smallest = min(self.data[parent], left, right)

            if smallest == self.data[parent]:
                break

            if smallest == left:
                self.data[parent], self.data[left_idx] = self.data[left_idx], self.data[parent]
                self.result.append('{parent} {left_idx}'.format(parent=parent, left_idx=left_idx))
                parent = left_idx

            if smallest == right:
                self.data[parent], self.data[right_idx] = self.data[right_idx], self.data[parent]
                self.result.append('{parent} {right_idx}'.format(parent=parent, right_idx=right_idx))
                parent = right_idx

    def build_heap(self):
        mid = self.size // 2 + 1
        for x in range(mid, -1, -1):
            self.sift_down(x)
        return self.result


def test():
    for num in range(4, 9):
        n, elements = open('./tests/0{}'.format(num)).read().splitlines()
        elements = list(map(int, elements.split()))

        m, *swaps = open('./tests/0{}.a'.format(num)).read().splitlines()

        min_heap = MinHeap(data=elements)
        result = min_heap.build_heap()

        assert len(result) == int(m)
        assert result == swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    min_heap = MinHeap(data=data)
    swaps = min_heap.build_heap()

    print(len(swaps))
    for pair in swaps:
        print(pair)


if __name__ == "__main__":
    # test()
    main()
