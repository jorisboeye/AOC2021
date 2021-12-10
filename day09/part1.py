from pathlib import Path

from aocd import submit


def parse_input(file):
    return [[int(c) for c in line] for line in file.read().splitlines()]


def neighbors(numbers, idx, line_length):
    for pos in [idx - line_length, idx - 1, idx + 1, idx + line_length]:
        if pos >= 0 and pos < len(numbers):
            yield numbers[pos]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    line_length = len(numbers[0])
    numbers = [n for line in numbers for n in line]
    result = 0
    for idx, number in enumerate(numbers):
        if number < min(neighbors(numbers, idx, line_length)):
            result += number + 1
    return result


if __name__ == "__main__":
    print(solve("input.txt"))
