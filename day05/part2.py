from collections import defaultdict
from pathlib import Path
from typing import NamedTuple

from aocd import submit


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_input(cls, text):
        return cls(*tuple(int(c) for c in text.split(",")))

    def __repr__(self):
        return f"{self.x},{self.y}"


class Line(NamedTuple):
    start: Point
    end: Point

    @classmethod
    def from_input(cls, text):
        return cls(*tuple(map(Point.from_input, text.split(" -> "))))

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    @property
    def points(self):
        if self.is_vertical:
            step = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))
            for y in range(self.start.y, self.end.y + step, step):
                yield Point(self.start.x, y)
        elif self.is_horizontal:
            step = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
            for x in range(self.start.x, self.end.x + step, step):
                yield Point(x, self.start.y)
        else:
            y_step = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))
            x_step = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
            y_range = range(self.start.y, self.end.y + y_step, y_step)
            x_range = range(self.start.x, self.end.x + x_step, x_step)
            for x, y in zip(x_range, y_range):
                yield Point(x, y)

    def __repr__(self):
        return f"{self.start}->{self.end}"


def parse_input(file):
    return [Line.from_input(line) for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        lines = parse_input(f)
    points = defaultdict(list)
    for line in lines:
        for point in line.points:
            points[point].append(line)
    return sum([1 for point in points if len(points[point]) > 1])


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 12:
        print(solve())  # , part="a", day=5)
