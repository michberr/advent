def clean_data(file):
    with open(file) as f:
        data = []
        for line in f.readlines():
            data.append([int(char) for char in line.strip()])
        return data


def part_1(data):
    minima = get_minima(data)

    return sum([data[i][j] + 1 for i,j in minima])


def part_2(data):
    minima = get_minima(data)
    basins = []

    for coordinate in minima:
        basin_size = traverse(coordinate, data)
        basins.append(basin_size)

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]

def traverse(coordinate, data):
    basin_size = 0
    possible_nodes = []
    visited = set()
    possible_nodes.append(coordinate)
    visited.add(coordinate)

    while possible_nodes:
        row, col = possible_nodes.pop()

        if data[row][col] != 9:
            basin_size += 1

            for neighbor in get_neighbors(data, row, col):
                if neighbor not in visited:
                    visited.add(neighbor)
                    possible_nodes.append(neighbor)
    return basin_size

def get_neighbors(data, row, col):
    above = (row-1, col) if row > 0 else None
    left = (row, col-1) if col > 0 else None
    right = (row, col+1) if col < (len(data[0]) - 1) else None
    below = (row+1, col) if row < (len(data) - 1) else None
    return [neighbor for neighbor in [above,left,right,below] if neighbor]

def get_minima(data):
    minima = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_low_point((i, j), data):
                minima.append((i, j))

    return minima


def is_low_point(coordinates, data):
    x, y = coordinates
    pt = data[x][y]
    neighbors = get_neighbors(data, x, y)

    for row, col in neighbors:
        if data[row][col] <= pt:
            return False

    return True


#********************************************************#
# Results
data = clean_data('input.txt')
print('part 1', part_1(data))
print('part 2', part_2(data))

# Test
print('RUNNING TESTS')
data = clean_data('test_input.txt')
assert part_1(data) == 15
assert part_2(data) == 1134
