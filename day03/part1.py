from pathlib import Path

from aocd import submit


def parse_input(file):
    return [list(line) for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    vals = [sum([int(n) for n in bits]) for bits in zip(*numbers)]
    result = [int((val) / len(numbers) > 0.5) for val in vals]
    gamma = sum([v * 2 ** p for p, v in enumerate(reversed(result))])
    epsilon = sum([(not v) * 2 ** p for p, v in enumerate(reversed(result))])

    return gamma * epsilon


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 198:
        submit(solve(), part="a", day=3)
