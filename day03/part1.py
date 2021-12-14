from pathlib import Path
from typing import Union

import pytest

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 198
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


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers = tuple(parse_lines(read(puzzle_input), target=list))
    vals = [sum([int(n) for n in bits]) for bits in zip(*numbers)]
    result = [int((val) / len(numbers) > 0.5) for val in vals]
    gamma = sum([v * 2 ** p for p, v in enumerate(reversed(result))])
    epsilon = sum([(not v) * 2 ** p for p, v in enumerate(reversed(result))])

    return gamma * epsilon


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
