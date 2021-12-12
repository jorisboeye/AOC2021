from collections import defaultdict
from pathlib import Path

from aocd import submit

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 36
SOLVED = False


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


def validate_connection(connection, path):
    if connection.isupper():
        return True
    elif connection != "end":
        lc = [c for c in path if c.islower()]
        return len(lc) - len(set(lc)) <= 1


def get_pathfinder(connections):
    def pathfinder(node, path):
        for connection in connections[node]:
            con_path = [n for n in path]
            if connection == "start":
                yield con_path + ["start"]
            elif validate_connection(connection, con_path + [connection]):
                yield from pathfinder(connection, con_path + [connection])

    return pathfinder


def solve(file: str = "input.txt"):
    connections = get_connections(parse_input(file))
    pathfinder = get_pathfinder(connections)
    paths = set()
    for path in pathfinder("end", ["end"]):
        if path:
            paths.add(tuple(path))
    return len(paths)


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
