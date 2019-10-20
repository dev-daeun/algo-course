# python3


class Query:
    def __init__(self, query):
        query = query.split()
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.text = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_amount):
        self.bucket_amount = bucket_amount
        self.table = [list() for _ in range(self.bucket_amount)]
        self.result = []

    def _hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_amount

    def add(self, text):
        hashed_key = self._hash(text)
        chain = self.table[hashed_key]
        for t in chain:
            if t == text:
                return
        chain.insert(0, text)

    def delete(self, text):
        hashed_key = self._hash(text)
        chain = self.table[hashed_key]
        for t in chain:
            if t == text:
                chain.remove(t)
                return

    def find(self, text):
        hashed_key = self._hash(text)
        chain = self.table[hashed_key]
        for t in chain:
            if t == text:
                return 'yes'
        return 'no'

    def check(self, ind):
        chain = self.table[ind]
        if not chain:
            return ''
        return ' '.join(chain)

    def process_query(self, query):
        if query.type == 'check':
            self.result.append(self.check(query.ind))
        if query.type == 'delete':
            self.delete(query.text)
        if query.type == 'find':
            self.result.append(self.find(query.text))
        if query.type == 'add':
            self.add(query.text)

    def process_queries(self):
        n = int(input())
        for _ in range(n):
            q = Query(input())
            self.process_query(q)
        for r in self.result:
            print(r)


def test():
    m, n, *queries = open('./tests/1').readlines()
    qs = QueryProcessor(int(m))

    for i in range(int(n)):
        query = Query(queries[i])
        qs.process_query(query)

    output = open('./tests/1.a').readlines()
    output = [o.strip('\n') for o in output]

    print(output)
    print(qs.result)
    assert ' '.join(qs.result) == ' '.join(output)


if __name__ == '__main__':
    # test()
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
