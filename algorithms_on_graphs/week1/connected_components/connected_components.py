#Uses python3
from collections import defaultdict


class Graph:

    def __init__(self, edges, vertex_count):
        self.vertex_adj_list = defaultdict(set)
        for edge in edges:
            self.vertex_adj_list[edge[0]].add(edge[1])
            self.vertex_adj_list[edge[1]].add(edge[0])
        for vertex in range(1, vertex_count + 1):
            if vertex not in self.vertex_adj_list:
                self.vertex_adj_list[vertex] = set()

    def reach(self, u):
        visited = set()
        to_visit = {u}
        reachables = {u}
        while to_visit:
            node = to_visit.pop()
            visited.add(node)
            for neighbor in self.vertex_adj_list[node]:
                if neighbor not in visited:
                    reachables.add(neighbor)
                    to_visit.add(neighbor)
        return reachables

    def connected_components(self):
        vertex_count = len(self.vertex_adj_list)
        components = defaultdict(set)
        visited = set()
        component_no = 1
        for vertex in range(1, vertex_count + 1):
            if vertex not in visited:
                reachables = self.reach(vertex)
                visited.update(reachables)
                components[component_no] = reachables
                component_no += 1
        return components


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        edges.append(edge)
    g = Graph(edges, vertex_count)
    print(len(g.connected_components()))


if __name__ == '__main__':
    main()
