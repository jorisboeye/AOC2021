from collections import Counter
from pathlib import Path
from typing import Union

from aoc.parsers import parse_lines, read, split_mapping

FILE = Path(__file__)
TEST_RESULT = 2188189693529


def solve(generations: int, file: Union[str, Path] = FILE.parent / "input.txt") -> int:
    template, rules_input = read(file).split("\n\n")
    pairs: Counter = Counter()
    for chars in zip(template, template[1:]):
        pairs["".join(chars)] += 1
    rules = dict(parse_lines(rules_input, split_mapping(" -> ")))
    for gen in range(generations):
        update: Counter = Counter()
        for pair, count in pairs.items():
            if pair in rules:
                for new_pair in (pair[0] + rules[pair], rules[pair] + pair[1]):
                    update[new_pair] += count
            else:
                update[pair] += count
        pairs = update
    counts: Counter = Counter()
    counts[template[0]] += 1
    counts[template[-1]] += 1
    for pair, count in pairs.items():
        for element in pair:
            counts[element] += count
    return (max(counts.values()) - min(counts.values())) // 2


if __name__ == "__main__":
    print(solve(40, FILE.parent / "test_input.txt"))
    print(solve(40, FILE.parent / "input.txt"))
