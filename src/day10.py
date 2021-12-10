from src.utilities import file_handling
from typing import List, Tuple, Set

pairs = {'<': '>',
         '{': '}',
         '[': ']',
         '(': ')'}
openers = pairs.keys()
closers = pairs.values()

scores = {'>': 25137,
          '}': 1197,
          ']': 57,
          ')': 3}

scores_pt2 = {'>': 4,
              '}': 3,
              ']': 2,
              ')': 1}


def check_syntax(openers_stack: List[str], remaining_command: str) -> Tuple[bool, str, List[str]]:
    if len(remaining_command) == 0:
        return True, '', list(reversed(openers_stack))
    else:
        this_char = remaining_command[0]
        if this_char in openers:
            openers_stack.append(this_char)
            return check_syntax(openers_stack, remaining_command[1:])
        else:
            possible_opener = openers_stack.pop()
            if pairs[possible_opener] == this_char:
                return check_syntax(openers_stack, remaining_command[1:])
            else:
                return False, this_char, list(reversed(openers_stack))


def check_all_lines_for_syntax_errors(program: List[str]) -> int:
    checked = [check_syntax([], command) for command in program]
    return sum([scores[failing_char] for valid, failing_char, _ in checked if not valid])


def pt2_score(remaining_chars: List[str]) -> int:
    score = 0
    for char in remaining_chars:
        score = score * 5 + scores_pt2[pairs[char]]
    return score


def check_all_lines_for_incomplete(program: List[str]) -> int:
    checked = [check_syntax([], command) for command in program]
    remaining = list(sorted([pt2_score(remaining_chars) for valid, _, remaining_chars in checked if valid]))
    mid = len(remaining) // 2
    return remaining[mid]


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day10')
    print(check_all_lines_for_syntax_errors(data))
    print(check_all_lines_for_incomplete(data))
