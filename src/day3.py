from src.utilities import file_handling
from typing import List


def calculate_commonest(input_data: List[str], bit_index: int) -> str:
    total = 0

    for element in input_data:
        if element[bit_index] == '1':
            total += 1
        else:
            total -= 1

    if total < 0:
        return '0'
    else:
        return '1'


def invert(value: str) -> str:
    output_value = ''
    for bit in value:
        if bit == '1':
            output_value += '0'
        else:
            output_value += '1'

    return output_value


def calculate_gamma(input: List[str]) -> str:
    length = len(input[0])
    gamma = ''

    for index in range(length):
        gamma += calculate_commonest(input, index)

    return gamma


def calculate_epsilon(gamma: str) -> str:
    return invert(gamma)


def bin_to_int(bin_string: str) -> int:
    return int('0b' + bin_string, base=2)


def check_bit(bit_number: int, input_data: List[str],  most: bool) -> str:
    commonest = calculate_commonest(input_data, bit_number)

    if most:
        goal = commonest
    else:
        goal = invert(commonest)

    remaining_input = list(filter(lambda x: x[bit_number] == goal, input_data))
    if len(remaining_input) == 1:
        return remaining_input[0]
    else:
        return check_bit(bit_number + 1, remaining_input, most)


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day3')
    gamma = calculate_gamma(data)
    epsilon = calculate_epsilon(gamma)
    print(bin_to_int(gamma) * bin_to_int(epsilon))
    oxygen = check_bit(0, data, True)
    co2 = check_bit(0, data, False)
    print(bin_to_int(oxygen) * bin_to_int(co2))

