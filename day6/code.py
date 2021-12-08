def clean_data(file):
    with open(file) as f:
        return [int(x) for x in f.read().strip().split(',')]


class FishPopulation():
    def __init__(self):
        self.fishes = []

    def add_fish(self, fish):
        self.fishes.append(fish)
        fish.population = self

    def pretty_print(self):
        print([fish.timer for fish in self.fishes])

    def count(self):
        return len(self.fishes)

    def grow(self, days):
        for day in range(days):
            for fish in self.fishes:
                fish.decrement_timer()


class Lanternfish():
    def __init__(self, timer):
        self.timer = timer
        self.population = None

    def decrement_timer(self):
        if self.timer == 0:
            self.timer = 6
            self.spawn_new_fish()
        else:
            self.timer -= 1

    def spawn_new_fish(self):
        fish = Lanternfish(9)  # will get decremented to 8 immediately
        self.population.add_fish(fish)


def part_1(data, days):
    population = FishPopulation()
    for timer in data:
        fish = Lanternfish(timer)
        population.add_fish(fish)

    population.grow(days)

    return population.count()


def part_2(data):
    pass


#********************************************************#
# Results
data = clean_data('input.txt')
print('part 1', part_1(data, 80))
# print('part 2', part_2(data, 256))

# Test
data = clean_data('test_input.txt')
assert part_1(data, 18) == 26
assert part_1(data, 80) == 5934
# assert part_2(data, 256) == 26984457539
