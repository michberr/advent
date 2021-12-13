def clean_data(file):
    with open(file) as f:
        return [int(x) for x in f.read().strip().split(',')]


def calculate_fuel_pt1(position, data):
    fuel = 0
    for crab in data:
        fuel += abs(crab - position)
    return fuel


def get_highest_position(data):
    highest = 0
    for pos in data:
        if pos > highest:
            highest = pos
    return pos


def calculate_lowest_fuel(data, fuel_func):
    highest_position = get_highest_position(data)
    lowest_fuel = None
    lowest_fuel_position = None

    for i in range(highest_position + 1):
        fuel = fuel_func(i, data)
        if not lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = i
        elif fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = i

    print('lowest fuel position', lowest_fuel_position)
    return lowest_fuel


def calculate_fuel_pt2(position, data):
    fuel = 0
    for crab in data:
        diff = abs(crab - position)
        fuel += sum(list(range(1, diff + 1)))
    return fuel


def part_1(data):
    return calculate_lowest_fuel(data, calculate_fuel_pt1)


def part_2(data):
    return calculate_lowest_fuel(data, calculate_fuel_pt2)

    #********************************************************#
    # Results
data = clean_data('input.txt')
print('part 1', part_1(data))
print('part 2', part_2(data))

# Test
print('RUNNING TESTS')
data = clean_data('test_input.txt')
assert part_1(data) == 37
assert part_2(data) == 168
