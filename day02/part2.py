from pathlib import Path
from re import X
from typing import NamedTuple

import attr
from aocd import submit


@attr.define
class Position:
    horizontal: int
    depth: int
    aim: int

    def move(self, direction, x):
        if direction == "forward":
            self.horizontal += int(x)
            self.depth += int(x) * self.aim
        elif direction == "down":
            self.aim += int(x)
        else:
            self.aim -= int(x)

    @property
    def result(self):
        return self.horizontal * self.depth


def parse_input(file):
    return [line.split() for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        instructions = parse_input(f)
    position = Position(0, 0, 0)
    for instruction in instructions:
        position.move(*instruction)
    return position.result


if __name__ == "__main__":
    print(solve())
    submit(solve(), part="b", day=2)
