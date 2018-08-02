# python3


class Node:

    def __init__(self, key, left_index, right_index):
        self.key = key
        self.left_index = left_index
        self.right_index = right_index
        self.left = None
        self.right = None


class Tree:

    def __init__(self, nodes):
        if nodes:
            self.root = Node(*nodes[0])
            stack = [self.root]
            while stack:
                current_node = stack.pop()
                if current_node.left_index > 0:
                    current_node.left = Node(*nodes[current_node.left_index])
                    stack.append(current_node.left)
                if current_node.right_index > 0:
                    current_node.right = Node(*nodes[current_node.right_index])
                    stack.append(current_node.right)
        else:
            self.root = None

    def in_order(self):
        result = []
        stack = [self.root]
        current = self.root
        while stack:
            while current:
                current = current.left
                stack.append(current)
            current = stack.pop()
            if current:
                result.append(current.key)
            if current and current.right:
                current = current.right
                stack.append(current)
            else:
                current = None
        return result

    def is_bst(self):
        if not self.root:
            return 'CORRECT'
        ordered = self.in_order()
        for i in range(len(ordered) - 1):
            if ordered[i] > ordered[i + 1]:
                return 'INCORRECT'
        return 'CORRECT'

    def get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.key

    def get_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current.key

    def is_bst_direct(self):
        if not self.root:
            return 'CORRECT'
        queue = [self.root]
        turn = 0
        while turn < len(queue):
            current = queue[turn]
            if current.left:
                queue.append(current.left)
                left_max = self.get_max(current.left)
                if left_max >= current.key:
                    return 'INCORRECT'
            if current.right:
                queue.append(current.right)
                right_min = self.get_min(current.right)
                if right_min < current.key:
                    return 'INCORRECT'
            turn += 1
        return 'CORRECT'


def main():
    n = int(input())
    nodes = []
    for i in range(n):
        key, left_ind, right_ind = [int(x) for x in input().split()]
        nodes.append((key, left_ind, right_ind))
    t = Tree(nodes)
    print(t.is_bst_direct())


main()
