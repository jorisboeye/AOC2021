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


def get_connections(lines):
    connections = defaultdict(set)
    for line in lines:
        connections[line[1]].add(line[0])
        connections[line[0]].add(line[1])
    return connections


def validate_connection(connection: str, path: Tuple[str, ...]) -> bool:
    if connection != "end":
        lc = [c for c in path if c.islower()]
        return len(lc) - len(set(lc)) <= 1
    else:
        return False


def get_pathfinder(connections: Dict[str, Set[str]]):
    def pathfinder(node: str, path: Tuple[str, ...]):
        for connection in connections[node]:
            if connection == "start":
                yield path + ("start",)
            elif validate_connection(connection, path + (connection,)):
                yield from pathfinder(connection, path + (connection,))

    return pathfinder


def solve(file: str = "input.txt"):
    pathfinder = get_pathfinder(get_connections(parse_input(file)))
    return len(set(pathfinder("end", ("end",))))


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        print(solution == SOLUTION)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
