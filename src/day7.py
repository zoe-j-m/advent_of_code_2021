from src.utilities import file_handling
from typing import List, Callable


def calculate_distance_pt1(pos:int, crab: int) -> int:
    return abs(pos - crab)


def calculate_distance_pt2(pos:int, crab: int) -> int:
    diff = abs(pos - crab)
    return diff * (diff + 1) // 2


def calculate_min_fuel(crabs: List[int], calculation_func: Callable[[int, int], int]) -> int:
    maximum_crabs = max(crabs)
    return min([sum([calculation_func(crab, pos) for crab in crabs]) for pos in range(maximum_crabs + 1)])


if __name__ == '__main__':
    data = file_handling.input_as_ints_from_single_line('data/day7')

    print(calculate_min_fuel(data, calculate_distance_pt1))
    print(calculate_min_fuel(data, calculate_distance_pt2))

