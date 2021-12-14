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


def solve(file: Union[str, Path] = FILE.parent / "input.txt") -> int:
    parts = read(file).split("\n\n")
    dots = set(parse_lines(parts[0], tuple_of_ints))
    result = 0
    for axis, datum in parse_lines(parts[1], lambda x: x.split()[-1].split("=")):
        dots = set(fold(dots, axis, int(datum)))
        result = len(dots) if not result else result
    return result


if __name__ == "__main__":
    print(solve(FILE.parent / "test_input.txt"))
    print(solve())
