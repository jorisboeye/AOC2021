from collections import defaultdict
from pathlib import Path

from aocd import submit


def get_segments(section):
    segments = defaultdict(set)
    for segment in section.strip().split():
        segments[len(segment)].add(frozenset(segment))
    return segments


def filter_segments(segments, content):
    for segment in segments:
        if content.issubset(segment):
            segments.remove(segment)
            return segment


def get_map(section):
    segments = get_segments(section=section)
    translation = {
        1: segments[2].pop(),
        4: segments[4].pop(),
        7: segments[3].pop(),
        8: segments[7].pop(),
    }
    translation[3] = filter_segments(segments[5], translation[1])
    translation[5] = filter_segments(segments[5], translation[4] - translation[1])
    translation[2] = segments[5].pop()
    translation[9] = filter_segments(segments[6], translation[3])
    translation[6] = filter_segments(segments[6], translation[5])
    translation[0] = segments[6].pop()
    return {v: str(k) for k, v in translation.items()}


def decode(section, mapping):
    return int("".join([mapping[frozenset(s)] for s in section.strip().split()]))


def parse_input(file):
    return [line.split("|") for line in file.read().splitlines()]


def solve(file: str = "input.txt"):
    with open(Path(__file__).parent / file, "r") as f:
        data = parse_input(f)
    solution = 0
    for digits, signal in data:
        mapping = get_map(section=digits)
        solution += decode(section=signal, mapping=mapping)
    return solution


if __name__ == "__main__":
    print(solve("input.txt"))
