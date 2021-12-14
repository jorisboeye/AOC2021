from functools import lru_cache
from pathlib import Path
from typing import Set

import pytest
from aocd import submit

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 195
SOLVED = True


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [[int(c) for c in line] for line in f.read().splitlines()]
    return list(n for line in numbers for n in line)


@lru_cache(maxsize=None)
def neighbors(idx: int) -> Set[int]:
    results = set()
    col = idx % 10
    positions = [idx + x for x in [-11, -10, -9, -1, 1, 9, 10, 11]]
    for pos in positions:
        poscol = pos % 10
        if pos >= 0 and pos < 100 and abs(poscol - col) < 2:
            results.add(pos)
    return results


def generate_flashers(numbers, flashed):
    for idx, n in enumerate(numbers):
        if n > 9 and idx not in flashed:
            yield idx


def board(numbers):
    board = ""
    for idx, number in enumerate(numbers):
        if not idx % 10:
            board += "\n"
        board += str(number)
    return board


def solve(file: str = "input.txt"):
    numbers = parse_input(file)
    # set generations:
    flashes = 0
    # print(board(numbers))
    flashed = set()
    generation = 0
    while len(flashed) < 100:
        # increase energy
        numbers = [n + 1 for n in numbers]
        # flash
        flashed = set()
        flashers = set(generate_flashers(numbers, flashed))
        while flashers:
            for idx in flashers:
                for neighbor in neighbors(idx) - flashers - flashed:
                    if neighbor not in (flashers | flashed):
                        numbers[neighbor] += 1
                flashed.add(idx)
            flashers = set(generate_flashers(numbers, flashed))
        # score flashes
        flashes += sum([n > 9 for n in numbers])
        # reset 9s
        numbers = [0 if n > 9 else n for n in numbers]
        # print(board(numbers))
        generation += 1
    return generation


@pytest.mark.parametrize(
    "numbers, idx, expected",
    (
        (list(range(100)), 0, {1, 10, 11}),
        (list(range(100)), 1, {0, 2, 10, 11, 12}),
        (list(range(100)), 10, {0, 1, 11, 20, 21}),
        (list(range(100)), 15, {4, 5, 6, 14, 16, 24, 25, 26}),
        (list(range(100)), 99, {88, 89, 98}),
    ),
)
def test_neighbors(numbers, idx, expected):
    assert neighbors(numbers, idx) == expected


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
