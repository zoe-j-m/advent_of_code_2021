from src.utilities import file_handling
from typing import List, Tuple
import re
from collections import Counter


def extract_from_strings(data: List[str]) -> List[Tuple[Tuple[int, int],Tuple[int,int]]]:
    matches = list(filter(None, map(lambda value: re.match(r'(\d+),(\d+) -> (\d+),(\d+)', value), data)))
    return list(map(lambda x: ((int(x.group(1)), int(x.group(2))), (int(x.group(3)), int(x.group(4)))), matches))


def coords_to_range(input: Tuple[Tuple[int, int],Tuple[int,int]]) -> List[Tuple[int, int]]:
    start, finish = input
    startx, starty = start
    finishx, finishy = finish

    if startx > finishx:
        stepx = -1
    elif startx == finishx:
        stepx = 0
    else:
        stepx = 1

    if starty > finishy:
        stepy = -1
    elif starty == finishy:
        stepy = 0
    else:
        stepy = 1

    output = []
    x = startx
    y = starty
    while x != finishx + stepx or y != finishy + stepy:
        output.append((x, y))
        x += stepx
        y += stepy

    return output


def find_multi_visited_cells(paths: List[List[Tuple[int,int]]]) -> int:
    print(paths)
    all_visited = []
    for path in paths:
        for cell in path:
            all_visited.append(cell)

    counts = Counter(all_visited)
    return len(list(filter(lambda x: x[1] > 1, counts.items())))


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day5')
    extracts = extract_from_strings(data)
    horivertipaths = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], extracts))
    paths = list(map(coords_to_range, horivertipaths))
    print(find_multi_visited_cells(paths))
    paths2 = list(map(coords_to_range, extracts))
    print(find_multi_visited_cells(paths2))
