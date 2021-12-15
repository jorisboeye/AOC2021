from pathlib import Path
from typing import Iterable, List, Set, Tuple, Union

import pytest

from aoc.parsers import read, tuple_of_ints
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 1924
TEST_INPUT = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

Board = Tuple[Tuple[int, ...], ...]


def columns(board: Board) -> List[Set[int]]:
    return [set(items) for items in zip(*board)]


def rows(board: Board) -> List[Set[int]]:
    return [set(line) for line in board]


def remaining(board: Board, drawn: Set[int]) -> Set[int]:
    return set.union(*columns(board)).difference(drawn)


def has_won(drawn: Set[int], board: Board) -> Set[int]:
    for direction in (columns, rows):
        for items in direction(board):
            if items.issubset(drawn):
                return remaining(board, drawn)
    return set()


def parse_board(board: str) -> Iterable[Tuple[int, ...]]:
    for line in board.splitlines():
        yield tuple(int(number) for number in line.split())


def solve(puzzle_input: Union[str, Path]) -> int:
    parts = read(puzzle_input).split("\n\n")
    numbers = tuple_of_ints(text=parts[0])
    boards = {tuple(parse_board(board)) for board in parts[1:]}
    drawn: Set[int] = set()
    won: Set[Board] = set()
    for draw in numbers:
        drawn.add(draw)
        for board in boards.difference(won):
            if remaining := has_won(drawn, board):
                won.add(board)
                if won == boards:
                    return int(sum(remaining) * draw)
    raise ValueError("Did not find solution.")


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
