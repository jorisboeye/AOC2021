from pathlib import Path
from statistics import median

from aocd import submit

OPENING = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSING = {")": 1, "]": 2, "}": 3, ">": 4}


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
                return 0
    score = 0
    for char in reversed(deck):
        score *= 5
        score += CLOSING[OPENING[char]]
    return score


def solve(file: str = "input.txt"):
    lines = parse_input(file)
    return median([score for line in lines if (score := check_line(line))])


if __name__ == "__main__":
    print(solve("test_input.txt"))
    print(solve("input.txt"))
