#Uses python3
from collections import defaultdict
from queue import PriorityQueue


class Graph:

    def __init__(self, edges, vertex_count):
        self.vertex_adj_list = defaultdict(set)
        for edge in edges:
            self.vertex_adj_list[edge[0]].add((edge[1], edge[2]))
        for vertex in range(1, vertex_count + 1):
            if vertex not in self.vertex_adj_list:
                self.vertex_adj_list[vertex] = set()

    def distance(self, start, end):
        if start == end:
            return 0
        distance_map = {}
        for vertex in range(1, len(self.vertex_adj_list) + 1):
            distance_map[vertex] = float('inf')
        distance_map[start] = 0
        qq = PriorityQueue()
        qq.put((0, start))
        while not qq.empty():
            dist, u = qq.get()
            if distance_map[u] != dist:
                continue
            for neighbor, weight in self.vertex_adj_list[u]:
                if distance_map[neighbor] > dist + weight:
                    distance_map[neighbor] = dist + weight
                    qq.put((dist + weight, neighbor))
        if distance_map[end] < float('inf'):
            return distance_map[end]
        return -1


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        edges.append(edge)
    start, end = [int(x) for x in input().split()]
    g = Graph(edges, vertex_count)
    print(g.distance(start, end))


if __name__ == '__main__':
    main()
