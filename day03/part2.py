from pathlib import Path

from aocd import submit


def parse_input(file):
    return [[int(n) for n in line] for line in file.read().splitlines()]


def oxygen_rating(numbers):
    for index_values in zip(*numbers):
        yield int(sum(index_values) / len(numbers) >= 0.5)


def co2_rating(numbers):
    for index_values in zip(*numbers):
        yield int(sum(index_values) / len(numbers) < 0.5)


def filter_numbers(numbers, rating_function):
    position = 0
    while len(numbers) > 1:
        rating = list(rating_function(numbers))
        numbers = [n for n in numbers if n[position] == rating[position]]
        position += 1
    return numbers[0]


def decimal(binary):
    return sum([v * 2 ** p for p, v in enumerate(reversed(binary))])


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        numbers = parse_input(f)
    return decimal(filter_numbers(numbers, oxygen_rating)) * decimal(
        filter_numbers(numbers, co2_rating)
    )


if __name__ == "__main__":
    print(solve("test_input.txt"))
    if solve("test_input.txt") == 230:
        submit(solve(), part="b", day=3)
