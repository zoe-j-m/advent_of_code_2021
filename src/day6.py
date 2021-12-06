from src.utilities import file_handling
from collections import Counter, Mapping


def process_day(days: Mapping[int, int]) -> Mapping[int, int]:
    new_day = {}
    for i in range(0, 9):
        if i == 0:
            new_day[8] = days[0]
            new_day[6] = days[0]
        elif i - 1 in new_day:
            new_day[i - 1] += days[i]
        else:
            new_day[i - 1] = days[i]

    return new_day


def total_fish(days: Mapping[int, int]) -> int:
    return sum(days.values())


def apply_days(day_count: int, days: Mapping[int, int]) -> Mapping[int, int]:
    current_days = days
    for i in range(day_count):
        current_days = process_day(current_days)
    return current_days


if __name__ == '__main__':
    data = list(map(lambda x: int(x), file_handling.input_as_string('data/day6').split(',')))
    start_days = Counter(data)
    end_days = apply_days(80, start_days)
    print(total_fish(end_days))
    end_days2 = apply_days(256, start_days)
    print(total_fish(end_days2))

