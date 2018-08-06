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

    def is_bipartite(self):
        """This assumes it is a connected graph"""
        queue = [1]
        q_ptr = 0
        color_map = {1: 0}
        while q_ptr < len(queue):
            node = queue[q_ptr]
            q_ptr += 1
            for neighbor in self.vertex_adj_list[node]:
                if color_map.get(neighbor) and color_map[neighbor] == color_map[node]:
                    return 0
                elif color_map.get(neighbor) is None:
                    queue.append(neighbor)
                    color_map[neighbor] = color_map[node] ^ 1
        return 1


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        if edge == (0, 0):
            break
        edges.append(edge)
    g = Graph(edges, vertex_count)
    print(g.is_bipartite())


if __name__ == '__main__':
    main()
