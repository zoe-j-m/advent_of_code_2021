from src.utilities import file_handling
from typing import List, Tuple, Dict, Set


def get_all_of_length(length: int, observed_values: List[Set[str]]) -> List[Set[str]]:
    return [observed for observed in observed_values if len(observed) == length]


def extract_data_from_line(line: str) -> Tuple[List[Set[str]], List[Set[str]]]:
    observed_and_output = line.split('|')
    return ([set(observed) for observed in observed_and_output[0].split()],
            [set(output_digit) for output_digit in observed_and_output[1].split()])


def decode_values(observed_values: List[Set[str]]) -> Dict[str, str]:
    single_values: Dict[str, str] = {}
    known_values: Dict[str, Set[str]] = {}

    known_values['cf'] = get_all_of_length(2, observed_values)[0]

    seven_value = get_all_of_length(3, observed_values)[0]
    single_values['a'] = [a_val for a_val in seven_value if a_val not in known_values['cf']][0]

    four_value = get_all_of_length(4, observed_values)[0]
    known_values['bd'] = set([bd_val for bd_val in four_value if bd_val not in known_values['cf']])

    length_five_values = get_all_of_length(5, observed_values)
    chars_in_all_length_five = list(
        set(length_five_values[0]) & set(length_five_values[1]) & set(length_five_values[2]))
    single_values['g'] = [g_val for g_val in chars_in_all_length_five if
                          g_val != single_values['a'] and g_val not in known_values['bd']][0]
    single_values['d'] = [d_val for d_val in chars_in_all_length_five if
                          d_val not in [single_values['a'], single_values['g']]][0]
    single_values['b'] = [b_val for b_val in known_values['bd'] if
                          b_val != single_values['d']][0]

    length_six_values = get_all_of_length(6, observed_values)
    chars_in_all_length_six = list(
        set(length_six_values[0]) & set(length_six_values[1]) & set(length_six_values[2]))
    single_values['f'] = [f_val for f_val in chars_in_all_length_six if f_val not in [
        single_values['a'], single_values['b'], single_values['g']]][0]
    single_values['c'] = [c_val for c_val in known_values['cf'] if c_val != single_values['f']][0]
    single_values['e'] = [e_val for e_val in
                          ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if e_val not in single_values.values()][0]

    return single_values


def decoded_value_to_intstr(encoded_value: Set[str], code: Dict[str, str]) -> str:
    decoder: Dict[str, str] = {coded: uncoded for uncoded, coded in code.items()}
    actuals = {
        'cf': '1',
        'acf': '7',
        'bcdf': '4',
        'acdeg': '2',
        'acdfg': '3',
        'abdfg': '5',
        'abdefg': '6',
        'abcefg': '0',
        'abcdfg': '9',
        'abcdefg': '8'
    }
    return actuals[''.join(list(sorted([decoder[coded_val] for coded_val in encoded_value])))]


def decode(observed_values: List[Set[str]], output_values: List[Set[str]]) -> int:
    coder = decode_values(observed_values)
    return int(''.join([decoded_value_to_intstr(output_val, coder) for output_val in output_values]))


def one_four_seven_eight_count(output_values: List[Set[str]]) -> int:
    one_four_seven_eight = [output_value for output_value in output_values if len(output_value) in [2, 3, 4, 7]]
    return len(one_four_seven_eight)


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day8')

    observed_and_output_values = [extract_data_from_line(line) for line in data]
    total_1478 = sum([one_four_seven_eight_count(output_values) for _, output_values in observed_and_output_values])
    print(total_1478)

    decoded_values = [decode(observed_and_output_value[0], observed_and_output_value[1]) for
                      observed_and_output_value in observed_and_output_values]
    print(sum(decoded_values))
