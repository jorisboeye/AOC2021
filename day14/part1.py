from collections import Counter
from pathlib import Path
from typing import Union

from aoc.parsers import parse_lines, read, split_mapping

FILE = Path(__file__)
TEST_RESULT = 1588


def solve(file: Union[str, Path] = FILE.parent / "input.txt") -> int:
    template, rules_input = read(file).split("\n\n")
    rules = dict(parse_lines(rules_input, split_mapping(" -> ")))
    for _ in range(10):
        new_template = template[0]
        for previous, current in zip(template, template[1:]):
            if (pair := "".join([previous, current])) in rules:
                new_template += rules[pair] + current
            else:
                new_template += current
        template = new_template
    counts: Counter = Counter(template)
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    test_solution = solve(FILE.parent / "test_input.txt")
    print(test_solution)
    if test_solution == TEST_RESULT:
        solution = solve()
        print(solution)
