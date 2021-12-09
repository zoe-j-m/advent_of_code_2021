from src.utilities import file_handling
from typing import List, Tuple, Set


def string_map_to_int_map(string_map: List[str]) -> List[List[int]]:
    return [[int(cell) for cell in row] for row in string_map]


def check_low_point(height_map: List[List[int]], pos: Tuple[int, int], max_x: int, max_y: int,
                    this_height: int) -> bool:
    is_lowest = True
    is_lowest = is_lowest and ((pos[0] == 0) or (height_map[pos[1]][pos[0] - 1] > this_height))
    is_lowest = is_lowest and ((pos[0] == max_x) or (height_map[pos[1]][pos[0] + 1] > this_height))
    is_lowest = is_lowest and ((pos[1] == 0) or (height_map[pos[1] - 1][pos[0]] > this_height))
    is_lowest = is_lowest and ((pos[1] == max_y) or (height_map[pos[1] + 1][pos[0]] > this_height))
    return is_lowest


def is_within_map(max_x: int, max_y: int, pos : Tuple[int, int]) -> bool:
    return 0 <= pos[0] <= max_x and 0 <= pos[1] <= max_y


def generate_basin_from_cell(cells_in_basin: Set[Tuple[int, int]], height_map: List[List[int]], pos: Tuple[int, int], max_x: int, max_y: int) -> Set[Tuple[int, int]]:
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    if is_within_map(max_x, max_y, pos) and height_map[pos[1]][pos[0]] != 9 and pos not in cells_in_basin:
        cells_in_basin.add(pos)
        checked = [cell for direction in directions for cell in generate_basin_from_cell(cells_in_basin, height_map, (pos[0] + direction[0], pos[1] + direction[1]), max_x, max_y)]
        return set(checked)
    else:
        return cells_in_basin


def get_lowest_points(height_map: List[List[int]], max_x: int, max_y: int) -> List[Tuple[Tuple[int, int], int]]:
    return [((col_number, row_number), cell) for row_number, row in enumerate(height_map) for col_number, cell in enumerate(row)
            if check_low_point(height_map, (col_number, row_number), max_x, max_y, cell)]


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day9')
    int_data = string_map_to_int_map(data)
    max_x = len(int_data[0]) - 1
    max_y = len(int_data) - 1

    all_lowest = get_lowest_points(int_data, max_x, max_y)
    print(sum([cell for _, cell in all_lowest]) + len(all_lowest))

    all_basins = set().union(
        {frozenset(generate_basin_from_cell(set(), int_data, pos, max_x, max_y)) for pos, _ in all_lowest})
    all_basin_sizes = sorted([len(basin) for basin in all_basins], reverse=True)
    print(all_basin_sizes[0] * all_basin_sizes[1] * all_basin_sizes[2])