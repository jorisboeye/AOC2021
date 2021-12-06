from pathlib import Path

from aocd import submit


def parse_input(file):
    return [int(line) for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    return numbers


if __name__ == "__main__":
    print(solve("test_input.txt"))
