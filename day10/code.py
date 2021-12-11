def clean_data(file):
    with open(file) as f:
        return [line.strip() for line in f.readlines()]

BRACKET_MAP = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

OPEN_BRACKET_SET = set(['(', '[', '{', '<'])


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


def part_1(data):
    illegal_chars = []

    syntax_error_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    for line in data:
        stack = Stack()
        for char in line:
            # opening char
            if char in OPEN_BRACKET_SET:
                stack.push(char)
            # valid closing char
            elif not stack.empty() and stack.peek() == BRACKET_MAP[char]:
                stack.pop()
            # corrupt line
            else:
                illegal_chars.append(char)
                break

    sum = 0
    for char in illegal_chars:
        sum += syntax_error_scores[char]

    return sum


def part_2(data):
    scores = []
    syntax_incomplete_scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    for line in data:
        stack = Stack()
        corrupt = False

        for char in line:
            # opening char
            if char in OPEN_BRACKET_SET:
                stack.push(char)
            # valid closing char
            elif not stack.empty() and stack.peek() == BRACKET_MAP[char]:
                stack.pop()
            # corrupted line
            else:
                corrupt = True
                break

        # incomplete line
        if not corrupt and not stack.empty():
            score = 0
            for item in reversed(stack.items):
                score = (score * 5) + syntax_incomplete_scores[item]
            scores.append(score)

    scores.sort()
    return scores[int(len(scores)/2)]


#********************************************************#
# Results
data = clean_data('input.txt')
print('part 1', part_1(data))
print('part 2', part_2(data))

# Test
print('RUNNING TESTS')
data = clean_data('test_input.txt')
assert part_1(data) == 26397
assert part_2(data) == 288957
