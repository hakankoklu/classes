# python3


class PhoneBook:

    def __init__(self):
        self.book = [None] * 10000000

    def run(self, query):
        parts = query.split()
        command = parts[0]
        number = int(parts[1])
        if command == 'find':
            result = self.book[number]
            return result or 'not found'
        elif command == 'del':
            self.book[number] = None
        else:
            self.book[number] = parts[2]


def process_queries(queries):
    book = PhoneBook()
    for query in queries:
        result = book.run(query)
        if result:
            print(result)


if __name__ == '__main__':
    number_of_queries = int(input())
    queries = []
    for _ in range(number_of_queries):
        queries.append(input())
    process_queries(queries)
