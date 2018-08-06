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

    def toposort(self):
        vertex_count = len(self.vertex_adj_list)
        visited = set()
        pre = {}
        post = {}
        click = 0
        for vertex in range(1, vertex_count + 1):
            if vertex in visited:
                continue
            to_visit = [vertex]
            parent_map = {}
            while to_visit:
                node = to_visit.pop()
                if node in visited:
                    continue
                pre[node] = click
                click += 1
                visited.add(node)
                to_add = self.vertex_adj_list[node] - visited
                if to_add:
                    for neighbor in to_add:
                        to_visit.append(neighbor)
                        parent_map[neighbor] = node
                else:
                    parent = node
                    while not self.vertex_adj_list[parent] - visited:
                        post[parent] = click
                        click += 1
                        if parent_map.get(parent):
                            parent = parent_map.pop(parent)
                        else:
                            break
        reverse_post_order = sorted(list(range(1, vertex_count + 1)), key=lambda x: post[x], reverse=True)
        return reverse_post_order
        # return pre, post


def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    edges = []
    for edge_index in range(edge_count):
        edge = tuple([int(x) for x in input().split()])
        if edge == (0, 0):
            break
        edges.append(edge)
    g = Graph(edges, vertex_count)
    # print(g.toposort())
    print(' '.join([str(x) for x in g.toposort()]))


if __name__ == '__main__':
    main()
