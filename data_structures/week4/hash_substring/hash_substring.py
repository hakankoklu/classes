# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def basic_hash(text):
    return sum([ord(x) for x in text])


def get_occurrences(pattern, text):
    hpattern = basic_hash(pattern)
    thash = basic_hash(text[:len(pattern)])
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        diff = ord(text[i + len(pattern) - 1]) - ord(text[i-1]) if i > 0 else 0
        thash = thash + diff
        if thash == hpattern and text[i:i + len(pattern)] == pattern:
            matches.append(i)
    return matches


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

