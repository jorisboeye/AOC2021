from pathlib import Path

from aocd import submit


def parse_input(file):
    return [int(line) for line in file.read().strip().split(",")]


def fuel_cost(position, target):
    return sum(range(abs(target - position) + 1))


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    min_value = 1e12
    for target in range(max(numbers)):
        total_distance = sum([fuel_cost(pos, target) for pos in numbers])
        if total_distance < min_value:
            min_value = total_distance
    return min_value


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 168:
        print(solve())
