from pathlib import Path
from typing import Union

import pytest

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 0
TEST_INPUT = """\

"""


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers = tuple(parse_lines(text=read(puzzle_input), target=int))
    return len(numbers)


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, TEST_RESULT),),
)
def test(test_input: str, expected: int) -> None:
    assert solve(test_input) == expected


if __name__ == "__main__":
    test_answer = solve(puzzle_input=FILE.parent / "test_input.txt")
    print(test_answer)
    if test_answer == TEST_RESULT:
        answer = solve(puzzle_input=FILE.parent / "input.txt")
        print(answer)
        submit(answer=answer, file=FILE)
