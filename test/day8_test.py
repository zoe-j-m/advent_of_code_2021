import unittest
from src.day8 import extract_data_from_line, one_four_seven_eight_count, decode

test_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


class Day8Test(unittest.TestCase):
    def test_partone(self):
        data = test_input.split('\n')
        observed_and_output_values = [extract_data_from_line(line) for line in data]
        total_1478 = sum([one_four_seven_eight_count(output_values) for _, output_values in observed_and_output_values])
        self.assertEqual(26, total_1478)

    def test_parttwp(self):
        data = test_input.split('\n')
        observed_and_output_values = [extract_data_from_line(line) for line in data]
        decoded_values = [decode(observed_and_output_value[0], observed_and_output_value[1]) for
                          observed_and_output_value in observed_and_output_values]
        self.assertEqual(61229, sum(decoded_values))


if __name__ == '__main__':
    unittest.main()
