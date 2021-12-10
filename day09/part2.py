import math
from functools import lru_cache
from pathlib import Path
from typing import Set, Tuple

import pytest


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [[int(c) for c in line] for line in f.read().splitlines()]
    line_length = len(numbers[0])
    return tuple(n for line in numbers for n in line), line_length


@lru_cache(maxsize=None)
def neighbors(numbers: Tuple[int], idx: int, line_length: int) -> Set[int]:
    results = set()
    positions = [idx - line_length, idx + line_length]
    if idx % line_length:
        positions.append(idx - 1)
    if (idx + 1) % line_length:
        positions.append(idx + 1)
    for pos in positions:
        if pos >= 0 and pos < len(numbers):
            results.add(pos)
    return results


def values(numbers: Tuple[int], idxs: Set[int]):
    return tuple(numbers[idx] for idx in idxs)


def check_idx(numbers: Tuple[int], idx: int, line_length: int, exclude: Set[int]):
    others = neighbors(numbers, idx, line_length) - exclude
    if numbers[idx] == 9 or (others and numbers[idx] > min(values(numbers, others))):
        return set()
    else:
        result = {idx}
        for neighbor in others:
            neighbor_result = check_idx(
                numbers=numbers,
                idx=neighbor,
                line_length=line_length,
                exclude=exclude | result,
            )
            result = result | neighbor_result
        return result


def solve(file: str = "input.txt"):
    numbers, line_length = parse_input(file)
    results = []
    for idx, _ in enumerate(numbers):
        bassin = check_idx(
            numbers=numbers, idx=idx, line_length=line_length, exclude=set()
        )
        results.append(len(bassin))
    return math.prod(sorted(results)[-3:])


@pytest.mark.parametrize(
    "numbers, idx, line_length, expected",
    (
        (tuple(range(9)), 0, 3, {1, 3}),
        (tuple(range(9)), 1, 3, {0, 2, 4}),
        (tuple(range(9)), 2, 3, {1, 5}),
        (tuple(range(9)), 3, 3, {0, 4, 6}),
        (tuple(range(9)), 4, 3, {1, 3, 5, 7}),
        (tuple(range(9)), 5, 3, {2, 4, 8}),
        (tuple(range(9)), 6, 3, {3, 7}),
        (tuple(range(9)), 7, 3, {4, 6, 8}),
        (tuple(range(9)), 8, 3, {5, 7}),
    ),
)
def test_neighbors(numbers, idx, line_length, expected):
    assert neighbors(numbers, idx, line_length) == expected


@pytest.mark.parametrize(
    "idx, expected", ((0, 0), (1, 3), (1, 3), (9, 9), (22, 14), (47, 0), (46, 9))
)
def test_check_idx(idx, expected):
    numbers, line_length = parse_input("test_input.txt")
    result = check_idx(numbers=numbers, idx=idx, line_length=line_length, exclude=set())
    assert len(result) == expected


if __name__ == "__main__":
    print(solve("input.txt"))
