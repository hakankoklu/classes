# python3


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def close_match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def check_brackets(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, start=1):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':

            if opening_brackets_stack and opening_brackets_stack[-1].close_match(next):
                opening_brackets_stack.pop()
            else:
                return i
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return 'Success'


if __name__ == "__main__":
    text = input()
    print(check_brackets(text))
