# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))
        self.result = []

    def merge(self, dst, src):
        pass


def test():
    for n in range(1, 3):
        _, rows, *queries = open(f'./tests/{n}').read().splitlines()
        queries = [q.split() for q in queries]
        db = Database(row_counts=[int(r) for r in rows.split()])

        for q in queries:
            dst, src = int(q[0]), int(q[1])
            db.merge(dst, src)
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
