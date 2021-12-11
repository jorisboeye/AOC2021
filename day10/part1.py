from pathlib import Path

from aocd import submit

OPENING = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSING = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse_input(file):
    with open(Path(__file__).parent / file, "r") as f:
        lines = f.read().splitlines()
    return lines


def check_line(line: str):
    deck = []
    for char in line:
        if char in OPENING:
            deck.append(char)
        elif char in CLOSING:
            if deck and deck[-1] in OPENING and OPENING[deck[-1]] == char:
                deck = deck[:-1]
            else:
                return CLOSING[char]
    return 0


def solve(file: str = "input.txt"):
    lines = parse_input(file)
    return sum([check_line(line) for line in lines])


if __name__ == "__main__":
    print(solve("test_input.txt"))
    print(solve("input.txt"))
