from pathlib import Path
from typing import List, Set

from aocd import submit


def columns(board: List[List[int]]):
    return [set(items) for items in zip(*board)]


def rows(board: List[List[int]]) -> List[Set[int]]:
    return [set(line) for line in board]


def remaining(board, drawn):
    return set.union(*columns(board)).difference(drawn)


def has_won(drawn: Set[int], board: List[List[int]]):
    for direction in (columns, rows):
        for items in direction(board):
            if items.issubset(drawn):
                return remaining(board, drawn)
    return 0


def parse_board(board):
    for line in board.splitlines():
        yield tuple(int(number) for number in line.split())


def parse_input(file):
    parts = file.read().split("\n\n")
    numbers = [int(number) for number in parts[0].split(",")]
    boards = {tuple(parse_board(board)) for board in parts[1:]}
    return numbers, boards


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers, boards = parse_input(f)
    drawn = set()
    for draw in numbers:
        drawn.add(draw)
        for board in boards:
            if remaining := has_won(drawn, board):
                return sum(remaining) * draw


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 4512:
        submit(solve(), part="a", day=4)
