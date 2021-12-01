from utilities import file_handling, sliding_window
from typing import List


def count_higher(depths : List[int]) -> int:
    previous = depths[0]
    higher = 0

    for depth in depths:
        if depth > previous:
            higher = higher + 1
        previous = depth

    return higher


def count_higher_sliding(depths : List[int]) -> int:
    slid_depths = list(map(lambda sublist : sum(sublist), sliding_window.window(3, depths)))
    return count_higher(slid_depths)


if __name__ == '__main__':
    data = file_handling.input_as_ints('data/day1')
    print(count_higher(data))
    print(count_higher_sliding(data))

