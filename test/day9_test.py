import unittest

from src.day9 import string_map_to_int_map, get_lowest_points, generate_basin_from_cell

test_input = '''2199943210
3987894921
9856789892
8767896789
9899965678'''


class Day9Test(unittest.TestCase):
    def test_partone(self):
        data = test_input.split('\n')
        int_data = string_map_to_int_map(data)
        max_x = len(int_data[0]) - 1
        max_y = len(int_data) - 1
        lowest_points = get_lowest_points(int_data, max_x, max_y)
        self.assertEqual(15, sum([cell for _, cell in lowest_points]) + len(lowest_points))

    def test_parttwo(self):
        data = test_input.split('\n')
        int_data = string_map_to_int_map(data)
        lowest_points = get_lowest_points(int_data)
        max_x = len(int_data[0]) - 1
        max_y = len(int_data) - 1
        print(generate_basin_from_cell(set(), int_data, (9, 0), max_x, max_y))
        all_basins = set().union({frozenset(generate_basin_from_cell(set(), int_data, pos, max_x, max_y)) for pos, _ in lowest_points})
        print(all_basins)
        all_basin_sizes = sorted([len(basin) for basin in all_basins], reverse= True)
        print(all_basin_sizes)
        self.assertEqual(1134, all_basin_sizes[0] * all_basin_sizes[1] * all_basin_sizes[2])


if __name__ == '__main__':
    unittest.main()
