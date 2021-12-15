from collections import defaultdict
from pathlib import Path
from typing import Iterable, NamedTuple, Union

import pytest

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 5
TEST_INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_input(cls, text: str) -> "Point":
        return cls(*tuple(int(c) for c in text.split(",")))

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"


class Line(NamedTuple):
    start: Point
    end: Point

    @classmethod
    def from_input(cls, text: str) -> "Line":
        return cls(*tuple(map(Point.from_input, text.strip().split(" -> "))))

    @property
    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def points(self) -> Iterable[Point]:
        if self.is_vertical:
            step = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))
            for y in range(self.start.y, self.end.y + step, step):
                yield Point(self.start.x, y)
        elif self.is_horizontal:
            step = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
            for x in range(self.start.x, self.end.x + step, step):
                yield Point(x, self.start.y)
        else:
            return

    def __repr__(self) -> str:
        return f"{self.start}->{self.end}"


def solve(puzzle_input: Union[str, Path]) -> int:
    lines = tuple(parse_lines(text=read(puzzle_input), target=Line.from_input))
    points = defaultdict(list)
    for line in lines:
        for point in line.points:
            points[point].append(line)
    return sum([1 for point in points if len(points[point]) > 1])


@pytest.mark.parametrize(
    ("test_input", "expected"),
    ((TEST_INPUT, TEST_RESULT),),
)
def test(test_input: str, expected: int) -> None:
    assert solve(test_input) == expected


if __name__ == "__main__":
    test_answer = solve(puzzle_input=TEST_INPUT)
    print(test_answer)
    if test_answer == TEST_RESULT:
        answer = solve(puzzle_input=FILE.parent / "input.txt")
        print(answer)
        submit(answer=answer, file=FILE)
