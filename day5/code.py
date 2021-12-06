def clean_data(file):
    with open(file) as f:
        data = []
        for line in f.readlines():
            split_line = [str.split(',') for str in line.strip().split(' -> ')]
            data.append([[int(str) for str in lst] for lst in split_line])
    return data


def part_1(data, board_size):
    return calculate_overlapping_vents(data, board_size)


def part_2(data, board_size):
    return calculate_overlapping_vents(data, board_size, False)


def calculate_overlapping_vents(data, board_size, skip_diagonals: True):
    grid = [[0] * board_size for n in range(board_size)]

    for row in data:
        [x1, y1], [x2, y2] = row
        # Make copies of coordinates
        xx1, yy1, xx2, yy2 = x1, y1, x2, y2

        # swap variables on the copies of x and y so we can still reference
        # the original
        if x1 > x2:
            xx1, xx2 = xx2, xx1
        if y1 > y2:
            yy1, yy2 = yy2, yy1

        xcoords = list(range(xx1, xx2 + 1))
        ycoords = list(range(yy1, yy2 + 1))

        pair = [xcoords[0], ycoords[0]]
        if pair != [x1, y1] and pair != [x2, y2]:
            xcoords.reverse()

        if len(xcoords) == 1:
            xcoords = xcoords * len(ycoords)
        if len(ycoords) == 1:
            ycoords = ycoords * len(xcoords)

        coord_pairs = list(zip(xcoords, ycoords))
        for x, y in coord_pairs:
            grid[y][x] += 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] >= 2:
                count += 1
    return count

#********************************************************#


# Results
data = clean_data('input.txt')
print('part 1', part_1(data, 1000))
print('part 2', part_2(data, 1000))

# Test
data = clean_data('test_input.txt')
assert part_1(data, 10) == 5
assert part_2(data, 10) == 12
