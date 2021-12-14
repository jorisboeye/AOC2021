from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, Tuple

from aocd import submit

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 36
SOLVED = True
SOLUTION = 98796


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        lines = [line.split("-") for line in f.read().splitlines()]
    return lines


def connections(lines):
    connections = defaultdict(set)
    for line in lines:
        connections[line[1]].add(line[0])
        connections[line[0]].add(line[1])
    return connections


def pathfinder(connections: Dict[str, Set[str]], node: str, path: Tuple[str, ...]):
    for connection in connections[node]:
        new_path = path + (connection,)
        if connection == "start":
            yield new_path
        elif (
            connection != "end"
            and len(lc := [c for c in new_path if c.islower()]) - len(set(lc)) <= 1
        ):
            yield from pathfinder(connections, connection, new_path)


def solve(file: str = "input.txt"):
    return len(set(pathfinder(connections(parse_input(file)), "end", ("end",))))


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        print(solution == SOLUTION)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
