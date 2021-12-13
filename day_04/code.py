BOARD_SIZE = 5


def clean_data(file):
    with open(file) as f:
        bingo_nums = list(
            map(lambda x: int(x), f.readline().strip().split(',')))
        boards = []

        for chunk in f.read().strip().split("\n\n"):
            board = [list(map(lambda x: int(x), str.split()))
                     for str in chunk.split('\n')]
            boards.append(board)
    return bingo_nums, boards


def part_1(bingo_nums, boards):
    for num in bingo_nums:
        winner, board = mark_boards_part1(boards, num)

        if winner:
            return num * calculate_sum(board)


def mark_boards_part1(boards, num):
    for board in boards:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == num:
                    board[i][j] = 'X'

                    if is_winner(board, i, j):
                        return True, board
    return False, None


def is_winner(board, row, col):
    if all(num == 'X' for num in board[row]):
        return True

    col_list = [row[col] for row in board]
    if all(num == 'X' for num in col_list):
        return True

    return False


def calculate_sum(board):
    sum = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 'X':
                sum += board[i][j]

    return sum


def part_2(bingo_nums, boards):
    board_wins = [False] * len(boards)

    for num in bingo_nums:
        winners = mark_boards_part2(boards, num, board_wins)

        if all(board_wins):
            if len(winners) > 1:
                raise('Two players won the last round')
            return num * calculate_sum(boards[winners[0]])


def mark_boards_part2(boards, num, board_wins):
    winners = []
    for x in range(len(boards)):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if boards[x][i][j] == num:
                    boards[x][i][j] = 'X'

                    if is_winner(boards[x], i, j) and not board_wins[x]:
                        winners.append(x)
                        board_wins[x] = True

    return winners

#********************************************************#


# Results
bingo_nums, boards = clean_data('input.txt')
assert len(bingo_nums) == 100
assert len(boards) == 100

print('part 1 winning score', part_1(bingo_nums, boards))

bingo_nums, boards = clean_data('input.txt')
print('part 2 winning score', part_2(bingo_nums, boards))

# Test
test_bingo, test_boards = clean_data('test_input.txt')
assert part_1(test_bingo, test_boards) == 4512
test_bingo, test_boards = clean_data('test_input.txt')
assert part_2(test_bingo, test_boards) == 1924
