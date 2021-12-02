from utilities import file_handling
import re
from typing import List, Tuple, Callable


def extract_from_strings(data: List[str]) -> List[Tuple[str, int]]:
    matches = list(filter(None, map(lambda value: re.match(r'(\w+) (\d+)', value), data)))
    return list(map(lambda x: (x.group(1), int(x.group(2))), matches))


def apply_change2(current_position: Tuple[int, int, int], instruction: Tuple[str, int]) -> Tuple[int, int, int]:
    (depth, horizontal, aim) = current_position
    (direction, distance) = instruction

    if direction == 'forward':
        horizontal += distance
        depth += aim * distance
    elif direction == 'down':
        aim += distance
    elif direction == 'up':
        aim -= distance

    return depth, horizontal, aim


def apply_change(current_position: Tuple[int, int, int], instruction: Tuple[str, int]) -> Tuple[int, int, int]:
    (depth, horizontal, aim) = current_position
    (direction, distance) = instruction

    if direction == 'forward':
        horizontal += distance
    elif direction == 'down':
        depth += distance
    elif direction == 'up':
        depth -= distance

    return depth, horizontal, aim


def apply_instructions(start: Tuple[int, int, int], instructions: List[Tuple[str, int]],
                       application: Callable[[Tuple[int, int, int], Tuple[str, int]], Tuple[int, int, int]]) -> \
        Tuple[int, int, int]:
    current_position = start
    for instruction in instructions:
        current_position = application(current_position, instruction)

    return current_position


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day2')
    end_depth, end_horizontal, _ = apply_instructions((0, 0, 0), extract_from_strings(data), apply_change)
    print(end_depth * end_horizontal)
    end_depth, end_horizontal, _ = apply_instructions((0, 0, 0), extract_from_strings(data), apply_change2)
    print(end_depth * end_horizontal)
