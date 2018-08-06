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

    def distance(self, start, end):
        if start == end:
            return 0
        queue = [start]
        q_ptr = 0
        distance_map = {start: 0}
        while q_ptr < len(queue):
            node = queue[q_ptr]
            q_ptr += 1
            for neighbor in self.vertex_adj_list[node]:
                if neighbor == end:
                    return distance_map[node] + 1
                if distance_map.get(neighbor) is None:
                    queue.append(neighbor)
                    distance_map[neighbor] = distance_map[node] + 1
        return -1


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        if edge == (0, 0):
            break
        edges.append(edge)
    start, end = [int(x) for x in input().split()]
    g = Graph(edges, vertex_count)
    print(g.distance(start, end))


if __name__ == '__main__':
    main()
