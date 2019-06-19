# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def dot_input():
    # expected result: 0, 1, 2 ... 9
    return [Segment(i, i) for i in range(100)]
    

def sparse_input():
    # expected result: 1, 6, 11
    return [
        Segment(1, 5),
        Segment(6, 10),
        Segment(11, 17),
    ]

def small_input():
    # expected result: 3
    return [
        Segment(1, 3),
        Segment(2, 5),
        Segment(3, 6),
    ]


def get_set(seg):
    return {t for t in range(seg.start, seg.end + 1)}

# Safe Move: 
# Find the farthest segment which satisfies intersected area with previous intersected area.
def optimal_points(segments):
    segments = sorted(segments, key=lambda s: s.start)
    start = 0
    sub_result = []
    n = len(segments)

    while start < n:
        intersected_seg = Segment(segments[start].start, segments[start].end)
        i = start + 1
        while i < n and segments[i].start - intersected_seg.end <= 0:
            intersected_seg = Segment(
                start=min([intersected_seg.end, segments[i].start]),
                end=intersected_seg.end,
            )
            i += 1
        sub_result.append(intersected_seg)
        start = i
    return [seg.start for seg in sub_result]    

    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
