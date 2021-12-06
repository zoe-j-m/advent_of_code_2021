from src.utilities import file_handling
from typing import List
from src.utilities.matrices import Matrix


def get_boards(data: List[str]) -> List[Matrix]:
    boards = []
    for i in range(2, len(data), 6):
        rows = list(map(lambda x: list(map(lambda y: int(y), x.split())), data[i:i+5]))
        boards.append(Matrix(rows))
    return boards


def check_winner(board: Matrix, winners: set[int]) -> bool:
    return any(set(row) <= winners for row in board.rows) or any(
        set(row) <= winners for row in board.transpose().rows)


def find_winners(all_winners: List[int], boards: List[Matrix], winner_try_count : int) -> (List[Matrix], List[int]):
    these_winners = all_winners[0:winner_try_count]
    winning_boards = list(filter(lambda x: check_winner(x, set(these_winners)), boards))
    if winning_boards:
        return winning_boards, these_winners
    else:
        return find_winners(all_winners, boards, winner_try_count + 1)


def find_winners2(all_winners: List[int], boards: set[Matrix], winner_try_count : int) -> (List[Matrix], List[int]):
    these_winners = all_winners[0:winner_try_count]
    winning_boards1 = set(filter(lambda x: check_winner(x, set(these_winners)), boards))
    if winning_boards1 and len(boards) == 1:
        return list(winning_boards1), these_winners
    else:
        remaining_boards = boards - winning_boards1
        return find_winners2(all_winners, remaining_boards, winner_try_count + 1)


if __name__ == '__main__':
    data = file_handling.input_as_lines('data/day4')
    winners = list(map(lambda x: int(x), data[0].split(',')))

    boards = get_boards(data)
    winning_boards, winners_at_win = find_winners(winners, boards, 1)
    unmarket = set(winning_boards[0].flatten()) - set(winners_at_win)

    a = sum(unmarket) * winners_at_win[-1]
    print(a)
    winning_boards2, winners_at_win2 = find_winners2(winners, set(boards), 1)
    unmarket2 = set(winning_boards2[0].flatten()) - set(winners_at_win2)

    b = sum(unmarket2) * winners_at_win2[-1]
    print(b)
