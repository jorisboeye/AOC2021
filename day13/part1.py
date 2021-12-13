from pathlib import Path
from typing import Tuple, Union

from aoc.parsers import parse_lines, read, tuple_of_ints

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 17
SOLVED = False


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [int(line) for line in f.read().splitlines()]
    return numbers


def fold(dot: Tuple[int, ...], axis: str, datum: int):
    if axis == "x" and (distance := dot[0] - datum) > 0:
        return datum - distance, dot[1]
    elif axis == "y" and (distance := dot[1] - datum) > 0:
        return dot[0], datum - distance
    else:
        return dot


def solve(file: Union[str, Path] = FILE.parent / "input.txt"):
    parts = read(file).split("\n\n")
    dots = set(parse_lines(parts[0], tuple_of_ints))
    result = 0
    for axis, datum in parse_lines(parts[1], lambda x: x.split()[-1].split("=")):
        dots = set(fold(dot, axis, int(datum)) for dot in dots)
        result = len(dots) if not result else result
    return result


if __name__ == "__main__":
    test_solution = solve(FILE.parent / "test_input.txt")
    print(test_solution)

    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
    #     if not SOLVED:
    #         submit(solution, part=PART, day=DAY)
