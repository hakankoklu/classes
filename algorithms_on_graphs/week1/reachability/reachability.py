#Uses python3
from collections import defaultdict


class Graph:

    def __init__(self, edges):
        self.vertex_adj_list = defaultdict(set)
        for edge in edges:
            self.vertex_adj_list[edge[0]].add(edge[1])
            self.vertex_adj_list[edge[1]].add(edge[0])

    def reach(self, u):
        visited = set()
        to_visit = {u}
        reachables = set()
        while to_visit:
            node = to_visit.pop()
            visited.add(node)
            for neighbor in self.vertex_adj_list[node]:
                if neighbor not in visited:
                    reachables.add(neighbor)
                    to_visit.add(neighbor)
        return reachables

    def is_reachable(self, u, v):
        if u == v:
            return 1
        reachables = self.reach(u)
        return int(v in reachables)


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        edges.append(edge)
    u, v = [int(x) for x in input().split()]
    g = Graph(edges)
    print(g.is_reachable(u, v))


if __name__ == '__main__':
    main()
