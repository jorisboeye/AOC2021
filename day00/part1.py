from pathlib import Path
from typing import Union

from aoc.parsers import parse_lines, read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 0


def solve(puzzle_input: Union[str, Path]) -> int:
    numbers = tuple(parse_lines(text=read(puzzle_input), target=int))
    return len(numbers)


if __name__ == "__main__":
    test_answer = solve(puzzle_input=FILE.parent / "test_input.txt")
    print(test_answer)
    if test_answer == TEST_RESULT:
        answer = solve(puzzle_input=FILE.parent / "input.txt")
        print(answer)
        submit(answer=answer, file=FILE)
