from pathlib import Path


def generate_increasing(numbers):
    for i, j in zip(numbers, numbers[1:]):
        yield j > i


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [int(line) for line in f.read().splitlines()]
    return sum(generate_increasing(numbers=numbers))


if __name__ == "__main__":
    print(solve())
