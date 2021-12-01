from pathlib import Path


def generate_increasing(numbers, step=1):
    for i, j in zip(numbers, numbers[step:]):
        yield j > i


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = [int(line) for line in f.read().splitlines()]
    return sum(generate_increasing(numbers=numbers, step=3))


if __name__ == "__main__":
    print(solve())
