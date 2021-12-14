from pathlib import Path
from typing import Union

import pytest

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 7
TEST_INPUT = """\
199
200
208
210
200
207
240
269
260
263
"""


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers = tuple(parse_lines(read(puzzle_input), target=int))
    return sum(j > i for i, j in zip(numbers, numbers[1:]))


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
