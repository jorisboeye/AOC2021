from pathlib import Path
from typing import Iterable, Set, Tuple, Union

from aoc.parsers import parse_lines, read, tuple_of_ints

FILE = Path(__file__)
Dot = Tuple[int, int]


def fold(dots: Set[Dot], axis: str, datum: int) -> Iterable[Dot]:
    for dot in dots:
        if axis == "x" and (distance := dot[0] - datum) > 0:
            yield datum - distance, dot[1]
        elif axis == "y" and (distance := dot[1] - datum) > 0:
            yield dot[0], datum - distance
        else:
            yield dot


def display(dots: Set[Dot]) -> Iterable[str]:
    for y in range(max(dot[1] for dot in dots) + 1):
        for x in range(max(dot[0] for dot in dots) + 1):
            yield "#" if (x, y) in dots else " "
        yield "\n"


def solve(file: Union[str, Path] = FILE.parent / "input.txt") -> str:
    parts = read(file).split("\n\n")
    dots = set(parse_lines(parts[0], tuple_of_ints))
    for axis, datum in parse_lines(parts[1], lambda x: x.split()[-1].split("=")):
        dots = set(fold(dots, axis, int(datum)))
    return "".join(display(dots))


if __name__ == "__main__":
    print(solve(FILE.parent / "test_input.txt"))
    print(solve())
