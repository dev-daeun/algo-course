# python3


class Database:

    def __init__(self, row_counts):
        # 1-index based
        self.row_counts = [0] + row_counts
        self.max_row_count = max(row_counts)
        self.parents = [i for i in range(len(self.row_counts) + 1)]
        self.ranks = [0 for _ in range(len(self.row_counts) + 1)]

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return self.max_row_count

        if self.ranks[first] > self.ranks[second]:
            return self.merge(dst=first_root, src=second_root)

        if self.ranks[first] == self.ranks[second]:
            self.ranks[first] += 1

        return self.merge(dst=second_root, src=first_root)

    def merge(self, dst, src):
        self.parents[src] = dst
        self.row_counts[dst] += self.row_counts[src]
        self.max_row_count = max(self.max_row_count, self.row_counts[dst])
        return self.max_row_count

    def find(self, table):
        # path compression
        p = table
        while self.parents[p] != p:
            p = self.parents[p]
        self.parents[table] = p
        return self.parents[table]


def test():
    for n in range(1, 4):
        _, rows, *queries = open('./tests/{n}'.format(n=n)).read().splitlines()
        queries = [q.split() for q in queries]
        db = Database(row_counts=[int(r) for r in rows.split()])
        result = []
        for q in queries:
            dst, src = int(q[0]), int(q[1])
            result.append(db.union(dst, src))

        assert result == list(map(int, open('./tests/{n}.a'.format(n=n)).read().splitlines()))


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(row_counts=counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.union(dst, src)
        print(db.max_row_count)


if __name__ == "__main__":
    # test()
    main()
