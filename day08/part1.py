from pathlib import Path

from aocd import submit


def parse_line(line):
    return [len(x) in [2, 3, 4, 7] for x in line.split("|")[-1].strip().split()]


def parse_input(file):
    return [sum(parse_line(line)) for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    return sum(numbers)


if __name__ == "__main__":
    print(solve("input.txt"))
