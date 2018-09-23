#Uses python3


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    trie = {0: {}}
    current_node = 0
    max_node = 0
    for pattern in patterns:
        for l in pattern:
            if l in trie[current_node]:
                current_node = trie[current_node][l]
            else:
                max_node += 1
                trie[current_node][l] = max_node
                current_node = max_node
                trie[current_node] = {}
        current_node = 0
    return trie


def main():
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())
    trie = build_trie(patterns)
    for node in trie:
        for c in trie[node]:
            print("{}->{}:{}".format(node, trie[node][c], c))


if __name__ == '__main__':
    main()
