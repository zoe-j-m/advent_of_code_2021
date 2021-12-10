import unittest

from src.day10 import check_all_lines_for_syntax_errors, check_all_lines_for_incomplete

test_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


class Day10Test(unittest.TestCase):
    def test_partone(self):
        data = test_input.split('\n')
        self.assertEqual(26397, check_all_lines_for_syntax_errors(data))

    def test_parttwo(self):
        data = test_input.split('\n')
        self.assertEqual(288957, check_all_lines_for_incomplete(data))


if __name__ == '__main__':
    unittest.main()
