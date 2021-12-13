def clean_data(file):
    with open(file) as f:
        folds = []
        data = []
        for line in f.readlines():
            if line[0:4] == 'fold':
                l = line.strip().replace('fold along ', '').split('=')
                folds.append((l[0], int(l[1])))
            else:
                l = line.strip().split(',')
                if len(l) > 1:
                    data.append([int(coord) for coord in l])

        return folds, data


class Board():
    def __init__(self, data):
        self.width = max([coord[0] for coord in data]) + 1
        self.length = max([coord[1] for coord in data]) + 1

        self.board = [['.'] * self.width for row in range(self.length)]
        self._plot_points(data)

    def _plot_points(self, data):
        for pt in data:
            self.board[pt[1]][pt[0]] = '#'

    def fold(self, instruction):
        direction, value = instruction

        if direction == 'x':
            # Remap the points
            for i in range(self.length):
                for j in range(value, self.width):
                    if self.board[i][j] == '#':
                        self.board[i][value - (j-value)] = '#'

            # slice the board
            self.board = [col[:value] for col in self.board]
        else:
            # Remap the points
            for i in range(value, self.length):
                for j in range(self.width):
                    if self.board[i][j] == '#':
                        self.board[value - (i-value)][j] = '#'

            # slice the board
            self.board = self.board[:value]

        self.update_dimensions()
        return self.board

    def update_dimensions(self):
        self.length = len(self.board)
        self.width = len(self.board[0])

    def count(self):
        return sum(x.count('#') for x in self.board)

    def pretty_print(self):
        for row in self.board:
            print(row)


def part_1(data, folds):
    board = Board(data)
    board.fold(folds[0])

    return board.count()


def part_2(data, folds):
    board = Board(data)
    for fold in folds:
        board.fold(fold)

    board.pretty_print()


#********************************************************#
# Results
folds, data = clean_data('input.txt')
print('part 1', part_1(data, folds))
print('part 2', part_2(data, folds))

# Test
print('RUNNING TESTS')
folds, data = clean_data('test_input.txt')
assert part_1(data, folds) == 17
print(part_2(data, folds))
