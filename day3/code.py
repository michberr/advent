import io


def clean_data(file):
    data = []
    with io.open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            data.append(line.strip())
    return data


def calculate_power_consumption(data):
    """Calculates power consumption (gamma * epsilon in decimal)"""

    gamma = []
    epsilon = []

    # Loop through each column in the binary strings and determine the gamma
    # and epsilon values (0 or 1) for that column; append to the gamma or
    # epsilon list.
    for bit in range(len(data[0])):
        col_data = list(map(lambda x: x[bit], data))
        col_gamma = calculate_gamma(col_data)
        col_eps = calculate_epsilon(col_data)
        gamma.append(col_gamma)
        epsilon.append(col_eps)

    gamma_dec = convert_binary_to_dec(''.join(gamma))
    epsilon_dec = convert_binary_to_dec(''.join(epsilon))

    return gamma_dec * epsilon_dec


def calculate_column(bit_list):
    """Counts the number of zeroes and ones in a list of bits"""
    zeroes = 0
    ones = 0
    for bit in bit_list:
        if bit == '0':
            zeroes += 1
        else:
            ones += 1

    return zeroes, ones


def calculate_gamma(bit_list):
    """Calculate gamma score for a column (list of bits)"""
    zeroes, ones = calculate_column(bit_list)
    if zeroes > ones:
        return '0'

    return '1'


def calculate_epsilon(bit_list):
    """Calculate epsilon score for a column (list of bits)"""
    zeroes, ones = calculate_column(bit_list)
    if zeroes > ones:
        return '1'

    return '0'


def convert_binary_to_dec(binary):
    """Converts a binary string into decimal"""
    dec = int(binary, 2)
    return dec


def calculate_life_support(data):
    """Calculates life support score (oxygen * CO2 in decimal)"""

    oxygen = calculate_life_support_measure(data, 'oxygen')
    co2 = calculate_life_support_measure(data, 'co2')

    oxygen_dec = convert_binary_to_dec(oxygen)
    co2_dec = convert_binary_to_dec(co2)
    return oxygen_dec * co2_dec


def calculate_life_support_measure(data, type):
    """Calculates a life support measure.

    Inputs:
        data: list of binary string data
        type: one of ('oxygen', 'co2')
    Output:
        a binary string representation of the life support measure
    """

    for bit in range(len(data[0])):
        col_data = list(map(lambda x: x[bit], data))
        if type == 'oxygen':
            result = calculate_gamma(col_data)
        elif type == 'co2':
            result = calculate_epsilon(col_data)

        # Filter data
        data = list(filter(lambda x: x[bit] == result, data))
        if len(data) == 1:
            return data[0]

#********************************************************#


# Results
data = clean_data('input.txt')
print('power', calculate_power_consumption(data))
print('life support', calculate_life_support(data))


# Test
test_data = ['00100',
             '11110',
             '10110',
             '10111',
             '10101',
             '01111',
             '00111',
             '11100',
             '10000',
             '11001',
             '00010',
             '01010']

assert calculate_power_consumption(test_data) == 198
assert calculate_life_support(test_data) == 230
