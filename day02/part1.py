from pathlib import Path
from typing import NamedTuple, Union

import pytest

from aoc.parsers import parse_lines, read, split_mapping
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 150
TEST_INPUT = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class Position(NamedTuple):
    horizontal: int
    vertical: int

    @property
    def result(self) -> int:
        return self.horizontal * self.vertical

    def move(self, direction: str, delta: str) -> "Position":
        if direction == "forward":
            delta_x = int(delta)
            delta_y = 0
        else:
            delta_x = 0
            delta_y = int(delta) if direction == "down" else -int(delta)

        return Position(
            horizontal=self.horizontal + delta_x, vertical=self.vertical + delta_y
        )


def solve(puzzle_input: Union[str, Path]) -> int:
    instructions = parse_lines(read(puzzle_input), split_mapping(" "))
    position = Position(0, 0)
    for instruction in instructions:
        position = position.move(*instruction)
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
