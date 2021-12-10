from pathlib import Path

from aocd import submit


def parse_input(file):
    return [int(line) for line in file.read().strip().split(",")]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    min_value = 1e6
    for position in range(max(numbers)):
        if (total_distance := sum([abs(n - position) for n in numbers])) < min_value:
            min_value = total_distance
    return min_value


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 37:
        print(solve())