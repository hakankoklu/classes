# python3


class Database:

    def __init__(self, n, row_counts):
        self.row_counts = row_counts
        self.parents = list(range(n))
        self.max_size = max(row_counts)

    def merge(self, destination, source):
        if destination != source:
            destination_parent = self.get_parent(destination)
            source_parent = self.get_parent(source)
            if destination_parent != source_parent:
                self.parents[source_parent] = destination_parent
                self.row_counts[destination_parent] += self.row_counts[source_parent]
                self.row_counts[source_parent] = 0
                self.max_size = max(self.max_size, self.row_counts[destination_parent])
                self.get_parent(source)

    def get_parent(self, table):
        internals = [table]
        while self.parents[table] != table:
            table = self.parents[table]
            internals.append(table)
        for t in internals:
            self.parents[t] = self.parents[table]
        return self.parents[table]


n, m = [int(x) for x in input().split()]
row_counts = [int(x) for x in input().split()]
db = Database(n, row_counts)
maxes = []
for i in range(m):
    destination, source = [int(x) for x in input().split()]
    db.merge(destination - 1, source - 1)
    maxes.append(db.max_size)
for i in range(len(maxes)):
    print(maxes[i])
