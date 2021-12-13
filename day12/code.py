def clean_data(file):
    with open(file) as f:
        data = [line.strip().split('-') for line in f.readlines()]
        cave_graph = create_cave_graph(data)

        return cave_graph


def part_1(graph):
    return traverse('start', set(['start']), graph)

def part_2(graph):
    return traverse('start', set(['start']), graph, True)


def traverse(current, visited, cave_graph, revisit_small_caves=False):
    if current == 'end':
        return 1

    count = 0

    for neighbor in cave_graph[current]:
        if neighbor.isupper():
            count += traverse(neighbor, visited, cave_graph, revisit_small_caves)
        elif neighbor not in visited:
            count += traverse(neighbor, visited.union({neighbor}), cave_graph, revisit_small_caves)
        elif revisit_small_caves and neighbor in visited and neighbor != 'start':
            count += traverse(neighbor, visited, cave_graph, False)

    return count


def create_cave_graph(data):
    cave_graph = {}

    # create graph
    for a,b in data:
        cave_graph[a] = cave_graph.get(a, list()) + [b]
        cave_graph[b] = cave_graph.get(b, list()) + [a]

    return cave_graph


#********************************************************#
# Results
data = clean_data('input.txt')
print('part 1', part_1(data))
print('part 2', part_2(data))

# Test
print('RUNNING TESTS')
data = clean_data('test_input1.txt')
assert part_1(data) == 10
assert part_2(data) == 36

data = clean_data('test_input2.txt')
assert part_1(data) == 19
assert part_2(data) == 103



