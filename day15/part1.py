from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path
from typing import Callable, Dict, List, Set, Tuple, Union

import pytest

from aoc import indexers
from aoc.parsers import parse_array, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 40
TEST_INPUT = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def reconstruct_path(came_from: Dict[int, int], current: int) -> List[int]:
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path = [current] + total_path
    return total_path


def get_heuristic(goal: int, line_length: int) -> Callable[[int], float]:
    ref_col = goal % line_length
    ref_row = goal // line_length

    def heuristic(idx: int) -> float:
        col = idx % line_length
        row = idx // line_length
        return ((ref_col - col) ** 2 + (ref_row - row) ** 2) ** 0.5

    return heuristic


def a_star(
    start: int,
    goal: int,
    h: Dict[int, float],
    d: Dict[int, int],
    neighbors: Callable[[int], Set[int]],
) -> List[int]:
    open_set: List[Tuple[float, int]] = []
    came_from: Dict[int, int] = dict()
    g_score: Dict[int, int] = defaultdict(lambda: 1_000_000)
    g_score[start] = 0
    f_score: Dict[int, float] = {start: h[start]}
    heappush(open_set, (f_score[start], start))
    while open_set:
        current = heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from=came_from, current=current)
        for neighbor in neighbors(current):
            tentative_g_score: int = g_score[current] + d[neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]
                heappush(open_set, (f_score[neighbor], neighbor))
    raise ValueError("No path found.")


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers, line_length = parse_array(text=read(puzzle_input), target=int)
    start = 0
    goal = len(numbers) - 1
    neighbors = indexers.neighbors(
        numbers=numbers, line_length=line_length, shape="diamond"
    )
    heuristic = get_heuristic(goal=goal, line_length=line_length)
    h = {idx: heuristic(idx) for idx in range(len(numbers))}
    d = dict(enumerate(numbers))
    path = a_star(start=start, goal=goal, h=h, d=d, neighbors=neighbors)
    score = sum(numbers[x] for x in path[1:])
    return score


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
