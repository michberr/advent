
from copy import deepcopy


def clean_data(file):
    with open(file) as f:
        data = []
        for line in f.readlines():
            data.append([int(char) for char in line.strip()])
        return data


def part_1(data, steps):
    data = deepcopy(data)
    flash_count = 0

    for step in range(steps):
        flash_count, _ = flash_all(data, flash_count)

    return flash_count

def part_2(data):
    data = deepcopy(data)
    steps = 1

    while True:
        _, flash_set = flash_all(data)

        if len(flash_set) == len(data) * len(data[0]):
            break
        steps += 1

    return steps


def flash_all(data, flash_count=0):
    # set to keep track of which indexes have flashed
    flash_set = set()

    # Increment all energy levels by 1
    for i in range(len(data)):
        for j in range(len(data)):
            data[i][j] += 1

    # Flash using a graph
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] > 9:
                flash_count, flash_set = flash_index((i,j), data, flash_count, flash_set)

    return flash_count, flash_set


def flash_index(coordinate, data, flash_count, flash_set):
    possible_nodes = [coordinate]

    while possible_nodes:
        row, col = possible_nodes.pop()

        if data[row][col] > 9:
            flash_set.add((row,col))
            flash_count += 1
            # Set value to 0 to prevent infinite flashing
            data[row][col] = 0

            for x,y in get_neighbors(data, row, col):
                if data[x][y] != 0:
                    data[x][y] += 1
                    if data[x][y] > 9:
                        possible_nodes.append((x,y))

    return flash_count, flash_set


def get_neighbors(data, row, col):
    above = (row-1, col) if row > 0 else None
    left = (row, col-1) if col > 0 else None
    right = (row, col+1) if col < (len(data[0]) - 1) else None
    below = (row+1, col) if row < (len(data) - 1) else None
    left_top = (row-1, col-1) if row > 0 and col > 0 else None
    right_top = (row-1, col+1) if row > 0 and col < (len(data[0]) - 1) else None
    left_bottom = (row+1, col-1) if row < (len(data) - 1) and col > 0 else None
    right_bottom = (row+1, col+1) if row < (len(data) - 1) and col < (len(data[0]) - 1) else None
    neighbors = [above, left, right, below, left_top, right_top, left_bottom, right_bottom]

    return [neighbor for neighbor in neighbors if neighbor]


#********************************************************#
# Results
data = clean_data('input.txt')
print('part 1', part_1(data, 100))
print('part 2', part_2(data))

# Test
print('RUNNING TESTS')
data = clean_data('test_input.txt')
assert part_1(data, 100) == 1656
assert part_2(data) == 195



