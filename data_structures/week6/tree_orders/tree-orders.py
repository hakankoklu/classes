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

    def pre_order(self):
        result = []
        stack = [self.root]
        current = self.root
        while stack:
            while current:
                result.append(current.key)
                current = current.left
                stack.append(current)
            current = stack.pop()
            if current and current.right:
                current = current.right
                stack.append(current)
            else:
                current = None
        return result

    def post_order(self):
        result = []
        stack = []
        done = False
        current = self.root
        while not done:
            if current:
                stack.append((current, False))
                current = current.left
            else:
                current, popped = stack.pop()
                if current and current.right and not popped:
                    stack.append((current, True))
                    current = current.right
                elif popped:
                    result.append(current.key)
                    current = None
                elif current:
                    result.append(current.key)
                    current = None
            done = len(stack) == 0
        return result

    def in_order_rec(self, node):
        result = []
        if node.left:
            left = self.in_order_rec(node.left)
            result.extend(left)
        result.append(node.key)
        if node.right:
            right = self.in_order_rec(node.right)
            result.extend(right)
        return result

    def pre_order_rec(self, node):
        result = [node.key]
        if node.left:
            left = self.pre_order_rec(node.left)
            result.extend(left)
        if node.right:
            right = self.pre_order_rec(node.right)
            result.extend(right)
        return result

    def post_order_rec(self, node):
        result = []
        if node.left:
            left = self.post_order_rec(node.left)
            result.extend(left)
        if node.right:
            right = self.post_order_rec(node.right)
            result.extend(right)
        result.append(node.key)
        return result


def main():
    n = int(input())
    nodes = []
    for i in range(n):
        key, left_ind, right_ind = [int(x) for x in input().split()]
        nodes.append((key, left_ind, right_ind))
    t = Tree(nodes)
    print(' '.join([str(x) for x in t.in_order()]))
    print(' '.join([str(x) for x in t.pre_order()]))
    print(' '.join([str(x) for x in t.post_order()]))


main()
