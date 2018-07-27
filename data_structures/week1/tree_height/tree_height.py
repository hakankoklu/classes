# python3


def compute_height(nodes, parent_ind):
    root = nodes[parent_ind]
    stack = [(root, 0)]
    max_depth = 0
    while stack:
        current_node, current_depth = stack.pop()
        max_depth = max(current_depth, max_depth)
        for child in current_node.children:
            stack.append((nodes[child], current_depth + 1))
    return max_depth + 1


class Node:

    def __init__(self, key):
        self.key = key
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return 'Key: {}\nChildren: {}\nParent: {}'.format(
            str(self.key),
            ', '.join([str(x) for x in self.children]),
            self.parent)


if __name__ == "__main__":
    number_of_nodes = int(input())
    parents = [int(x) for x in input().split()]
    nodes = [Node(x) for x in range(number_of_nodes)]
    parent_ind = 0
    for i, parent in enumerate(parents):
        nodes[i].parent = parent
        if parent != -1:
            nodes[parent].add_child(i)
        else:
            parent_ind = i
    print(compute_height(nodes, parent_ind))
