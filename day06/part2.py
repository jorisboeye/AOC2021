from collections import defaultdict
from pathlib import Path

from aocd import submit


def parse_input(file):
    return [int(line) for line in file.read().split(",")]


def new_genaration(previous):
    for days, fish in previous.items():
        if days == 0:
            yield 8, fish
        else:
            yield days - 1, fish


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    fish = {}
    fish[0] = defaultdict(lambda: 0)
    for number in numbers:
        fish[0][number] += 1
    for generation in range(256):
        fish[generation + 1] = defaultdict(lambda: 0, new_genaration(fish[generation]))
        fish[generation + 1][6] += fish[generation + 1][8]
    # return fish
    return sum([fish[256][days] for days in fish[256]])


if __name__ == "__main__":
    print(solve("input.txt"))
