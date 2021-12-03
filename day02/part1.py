from pathlib import Path
from typing import NamedTuple

from aocd import submit


class Position(NamedTuple):
    horizontal: int
    vertical: int

    @property
    def result(self):
        return self.horizontal * self.vertical


def move(position, direction, delta):
    if direction == "forward":
        return Position(
            horizontal=position.horizontal + int(delta), vertical=position.vertical
        )
    elif direction == "down":
        return Position(
            horizontal=position.horizontal, vertical=position.vertical + int(delta)
        )
    else:
        return Position(
            horizontal=position.horizontal, vertical=position.vertical - int(delta)
        )


def parse_input(file):
    return [line.split() for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        instructions = parse_input(f)
    position = Position(0, 0)
    for instruction in instructions:
        position = move(position, *instruction)
    return position.result


if __name__ == "__main__":
    print(solve())
    submit(solve(), part="a", day=2)
