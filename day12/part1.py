from collections import defaultdict
from pathlib import Path

from aocd import submit

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 10
SOLVED = True
SOLUTION = 3410


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


def get_pathfinder(connections):
    def pathfinder(node, path):
        for connection in connections[node]:
            con_path = [n for n in path]
            if connection == "start":
                yield con_path + ["start"]
            elif connection.isupper() or connection not in con_path:
                yield from pathfinder(connection, con_path + [connection])

    return pathfinder


def solve(file: str = "input.txt"):
    connections = get_connections(parse_input(file))
    pathfinder = get_pathfinder(connections)
    paths = []
    for path in pathfinder("end", ["end"]):
        if path:
            paths.append(path)
    return len(paths)


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        print(solution == SOLUTION)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
