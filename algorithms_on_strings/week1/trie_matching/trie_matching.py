# python3


def solve(text, trie):
    # print(trie)
    result = []
    for ind in range(len(text)):
        current_node = 0
        start_ind = ind
        moving_ind = ind
        while True:
            if moving_ind >= len(text):
                break
            if text[moving_ind] in trie[current_node]:
                current_node = trie[current_node][text[moving_ind]]
                moving_ind += 1
                if trie[current_node] == {}:
                    result.append(start_ind)
                    break
            else:
                break
    return result


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
    text = input()
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())
    trie = build_trie(patterns)
    indices = solve(text, trie)
    print(' '.join([str(x) for x in indices]))


if __name__ == '__main__':
    main()
