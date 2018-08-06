#Uses python3
from collections import defaultdict


class Graph:

    def __init__(self, edges, vertex_count):
        self.vertex_adj_list = defaultdict(set)
        for edge in edges:
            self.vertex_adj_list[edge[0]].add(edge[1])
        for vertex in range(1, vertex_count + 1):
            if vertex not in self.vertex_adj_list:
                self.vertex_adj_list[vertex] = set()
        # print(self.vertex_adj_list)

    def has_cycle(self):
        vertex_count = len(self.vertex_adj_list)
        checked = set()
        for vertex in range(1, vertex_count + 1):
            if vertex in checked:
                continue
            # print('Checking: ', vertex)
            visited = set()
            to_visit = [vertex]
            parent_map = {}
            while to_visit:
                node = to_visit.pop()
                # print('Visiting: ', node)
                visited.add(node)
                checked.add(node)
                intersect = self.vertex_adj_list[node].intersection(visited)
                if intersect:
                    return True
                unchecked_neighbors = self.vertex_adj_list[node] - checked
                # print('Visited so far: ', visited)
                if unchecked_neighbors:
                    for neighbor in unchecked_neighbors:
                        parent_map[neighbor] = node
                        to_visit.append(neighbor)
                else:
                    parent = node
                    while not self.vertex_adj_list[parent] - checked:
                        visited.remove(parent)
                        if parent_map.get(parent):
                            parent = parent_map.pop(parent)
                        else:
                            break
                # print('Visited so far: ', visited)
                # print('To visit:', to_visit)
                # print('Checked: ', checked)
        return False


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
    # while True:
        edge = tuple([int(x) for x in input().split()])
        if edge == (0, 0):
            break
        edges.append(edge)
    g = Graph(edges, vertex_count)
    print(int(g.has_cycle()))


if __name__ == '__main__':
    main()
