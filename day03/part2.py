from pathlib import Path
from typing import Callable, Iterable, List, Tuple, Union

import pytest

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 230
TEST_INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

Numbers = Tuple[List[int], ...]


def oxygen_rating(numbers: Numbers) -> Iterable[int]:
    for index_values in zip(*numbers):
        yield int(sum(index_values) / len(numbers) >= 0.5)


def co2_rating(numbers: Numbers) -> Iterable[int]:
    for index_values in zip(*numbers):
        yield int(sum(index_values) / len(numbers) < 0.5)


def filter_numbers(
    numbers: Numbers, rating_function: Callable[[Numbers], Iterable[int]]
) -> List[int]:
    position = 0
    while len(numbers) > 1:
        rating = tuple(rating_function(numbers))
        numbers = tuple(n for n in numbers if n[position] == rating[position])
        position += 1
    return numbers[0]


def decimal(binary: List[int]) -> int:
    return sum([v * 2 ** p for p, v in enumerate(reversed(binary))])


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers = tuple(
        parse_lines(read(puzzle_input), target=lambda x: [int(n) for n in x])
    )
    return decimal(filter_numbers(numbers, oxygen_rating)) * decimal(
        filter_numbers(numbers, co2_rating)
    )


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, TEST_RESULT),),
)
def test(test_input: str, expected: int) -> None:
    assert solve(test_input) == expected


if __name__ == "__main__":
    test_answer = solve(TEST_INPUT)
    if test_answer == TEST_RESULT:
        answer = solve(FILE.parent / "input.txt")
        submit(answer=answer, file=FILE)
    else:
        print(test_answer)
