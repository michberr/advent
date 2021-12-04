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
    marking_boards = setup_marking_boards(len(bingo_nums))

    for num in bingo_nums:
        winner, board_num = mark_boards_part1(boards, marking_boards, num)

        if winner:
            sum = 0
            board = boards[board_num]
            marked_board = marking_boards[board_num]

            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if marked_board[i][j] == 0:
                        sum += board[i][j]
            return num * sum


def setup_marking_boards(num):
    return [[[0, 0, 0, 0, 0]
             for i in range(BOARD_SIZE)] for j in range(num)]


def mark_boards_part1(boards, mark_boards, num):
    for x in range(len(boards)):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if boards[x][i][j] == num:
                    mark_boards[x][i][j] = 1

                    if is_winner(mark_boards[x], i, j):
                        return True, x
    return False, None


def is_winner(board, row, col):
    if all(num == 1 for num in board[row]):
        return True

    col_list = [row[col] for row in board]
    if all(num == 1 for num in col_list):
        return True

    return False


def part_2(bingo_nums, boards):
    board_wins = [False] * len(boards)

    mark_boards = setup_marking_boards(len(bingo_nums))

    for num in bingo_nums:
        winners = mark_boards_part2(boards, mark_boards, num, board_wins)

        if all(board_wins):
            if len(winners) > 1:
                raise('Two players won the last round')

            winner = winners[0]
            board = boards[winner]
            mark_board = mark_boards[winner]
            sum = 0

            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if mark_board[i][j] == 0:
                        sum += board[i][j]
            return num * sum


def mark_boards_part2(boards, mark_boards, num, board_wins):
    winners = []
    for x in range(len(boards)):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if boards[x][i][j] == num:
                    mark_boards[x][i][j] = 1

                    if is_winner(mark_boards[x], i, j) and not board_wins[x]:
                        winners.append(x)
                        board_wins[x] = True

    return winners

#********************************************************#


# Results
bingo_nums, boards = clean_data('input.txt')
assert len(bingo_nums) == 100
assert len(boards) == 100

print('part 1 winning score', part_1(bingo_nums, boards))
print('part 2 winning score', part_2(bingo_nums, boards))

# Test
test_bingo, test_boards = clean_data('test_input.txt')
assert part_1(test_bingo, test_boards) == 4512
assert part_2(test_bingo, test_boards) == 1924
