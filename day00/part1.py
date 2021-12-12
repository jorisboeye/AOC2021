from pathlib import Path

from aocd import submit

FILE = Path(__file__)
PART = "a" if FILE.stem == "part1" else "b"
DAY = int(FILE.parent.stem[-2:])
TEST_RESULT = 0
SOLVED = False


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [int(line) for line in f.read().splitlines()]
    return numbers


def solve(file: str = "input.txt"):
    numbers = parse_input(file)
    return numbers


if __name__ == "__main__":
    test_solution = solve("test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
        if not SOLVED:
            submit(solution, part=PART, day=DAY)
