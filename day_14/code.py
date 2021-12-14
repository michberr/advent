from collections import Counter

def clean_data(file):
    with open(file) as f:
        template = f.readline().strip()
        # blank line
        f.readline()

        map = {}
        for line in f.readlines():
            k, v = line.strip().split(' -> ')
            map[k] = v

    return template, map

######## Part 1 ###############
# OOP solution is good enough and more readable


class Polymer():
    def __init__(self, map, template):
        self.map  = map
        self.template = template

    def grow(self):
        new_polymer = [self.template[0]]

        for i in range(len(self.template) - 1):
            v = map[self.template[i] + self.template[i+1]]
            new_polymer.extend([v, self.template[i+1]])

        self.template = new_polymer

    def to_string(self):
        return ''.join(self.template)

    def length(self):
        return len(self.template)

    def tally(self):
        c = Counter(self.template)
        return c.most_common()[0][1] - c.most_common()[-1][1]



def part_1(template, map):
    polymer = Polymer(map, list(template))
    for i in range(10):
        polymer.grow()

    return polymer.tally()


######## Part 2 ###############
# OOP solution is not performant enough, use counters instead


def part_2(template, map, rounds):
    tail_letters = set([template[0], template[-1]])
    letter_pairs = Counter()

    # Initialize counter with counts of every two letter combo
    for i in range(len(template) - 1):
        k = template[i] + template[i+1]
        letter_pairs.update({k: 1})


    for i in range(rounds):
        round_counts = Counter()
        for k,v in letter_pairs.items():
            first_letter, second_letter = k
            new_pair_1 = first_letter + map[k]
            new_pair_2 = map[k] + second_letter

            round_counts.update({new_pair_1: v, new_pair_2: v})

        letter_pairs = round_counts

    freqs = get_letter_frequencies(letter_pairs, tail_letters)

    # gut check
    print(freqs)
    print('length', sum(freqs.values()))

    return freqs.most_common()[0][1] - freqs.most_common()[-1][1]


def get_letter_frequencies(counter, tail_letters):
    letter_counts = Counter()

    # Tally the letter frequencies from the letter pairs
    for k,v in counter.items():
        first_letter, second_letter = k
        letter_counts[first_letter] = letter_counts.get(first_letter, 0) + v
        letter_counts[second_letter] = letter_counts.get(second_letter, 0) + v

    for letter, count in letter_counts.items():
        # Tail letters have 1 more than double the frequency
        if letter in tail_letters:
            letter_counts[letter] = int((count - 1)/2 + 1)
        # non-tail letters were doubled
        else:
            letter_counts[letter] = int(count/2)

    return letter_counts

#********************************************************#
# Results
template, map = clean_data('input.txt')
print('part 1', part_1(template, map))
print('part 2', part_2(template, map, 40))

# Test
print('RUNNING TESTS')
template, map = clean_data('test_input.txt')
assert part_1(template, map) == 1588
assert part_2(template, map, 40) == 2188189693529