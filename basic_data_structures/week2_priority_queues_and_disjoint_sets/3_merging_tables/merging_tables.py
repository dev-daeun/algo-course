# python3


class Database:

    def __init__(self, row_counts):
        self.row_counts = [0]
        self.row_counts.extend(row_counts)
        self.max_row_counts = max(self.row_counts)
        self.result = []
        self.parents = [i for i in range(len(self.row_counts) + 1)]

    def union(self, dst, src):
        dst_root = self.find(dst)
        src_root = self.find(src)

        if dst_root == src_root:
            self.result.append(self.max_row_counts)
            return

        self.parents[src_root] = dst_root
        self.row_counts[dst_root] += self.row_counts[src_root]
        self.max_row_counts = max(self.max_row_counts, self.row_counts[dst_root])
        self.result.append(self.max_row_counts)

    def find(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.find(self.parents[table])
        return self.parents[table]


def test():
    for n in range(1, 4):
        _, rows, *queries = open(f'./tests/{n}').read().splitlines()
        queries = [q.split() for q in queries]
        db = Database(row_counts=[int(r) for r in rows.split()])

        for q in queries:
            dst, src = int(q[0]), int(q[1])
            db.union(dst, src)

        assert db.result == list(map(int, open(f'./tests/{n}.a').read().splitlines()))


def main():
    test()
    # n_tables, n_queries = map(int, input().split())
    # counts = list(map(int, input().split()))
    # assert len(counts) == n_tables
    # db = Database(counts)
    # for i in range(n_queries):
    #     dst, src = map(int, input().split())
    #     db.merge(dst - 1, src - 1)
    #     print(db.max_row_count)


if __name__ == "__main__":
    main()
