from pathlib import Path
from typing import Union

import attr
import pytest

from aoc.parsers import parse_lines, read, split_mapping
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 900
TEST_INPUT = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@attr.s(auto_attribs=True)
class Position:
    horizontal: int
    depth: int
    aim: int

    def move(self, direction: str, x: str) -> None:
        if direction == "forward":
            self.horizontal += int(x)
            self.depth += int(x) * self.aim
        elif direction == "down":
            self.aim += int(x)
        else:
            self.aim -= int(x)

    @property
    def result(self) -> int:
        return self.horizontal * self.depth


def solve(puzzle_input: Union[str, Path]) -> int:
    instructions = parse_lines(read(puzzle_input), split_mapping(" "))
    position = Position(0, 0, 0)
    for instruction in instructions:
        position.move(*instruction)
    return position.result


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
