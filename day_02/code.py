import io


def clean_data(file):
    data = []
    with io.open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            data.append(line.split())
    return data


def calculate_position(data):
    depth = 0
    position = 0

    for command in data:
        direction = command[0]
        distance = int(command[1])

        if direction == 'forward':
            position += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance

    return depth * position


def calculate_position_with_aim(data):
    depth = 0
    position = 0
    aim = 0

    for command in data:
        direction = command[0]
        distance = int(command[1])

        if direction == 'forward':
            position += distance
            depth += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

    return depth * position


data = clean_data('data.txt')
print('position', calculate_position(data))
print('position with aim', calculate_position_with_aim(data))


# test
test_data = [
    ['forward', 5],
    ['down', 5],
    ['forward', 8],
    ['up', 3],
    ['down', 8],
    ['forward', 2]
]
assert 900 == calculate_position_with_aim(test_data)
