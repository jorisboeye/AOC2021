import textwrap
from math import prod
from pathlib import Path
from typing import Callable, Dict, List, Tuple, Union

import pytest

from aoc.parsers import read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 1
TEST_INPUTS = (
    ("5401A90002191062DC1C1007625C718A", 0),
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1),
)


def greater_than(x: List[int]) -> int:
    if len(x) != 2:
        raise ValueError(f"Greater than should have 2 subpackages, has <{len(x)}>.")
    else:
        return int(x[0] > x[1])


def less_than(x: List[int]) -> int:
    if len(x) != 2:
        raise ValueError(f"Less than should have 2 subpackages, has <{len(x)}>.")
    else:
        return int(x[0] < x[1])


def equal(x: List[int]) -> int:
    if len(x) != 2:
        raise ValueError(f"Equal should have 2 subpackages, has <{len(x)}>.")
    else:
        return int(x[0] == x[1])


OPERATIONS: Dict[int, Callable[[List[int]], int]] = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: greater_than,
    6: less_than,
    7: equal,
}


def hex_to_bits(text: str) -> str:
    return "".join((f"{int(h, 16):04b}" for h in text))


def parse_section(bits: str, length: int) -> Tuple[str, int]:
    return bits[length:], int(bits[:length], 2)


def parse_literal(bits: str) -> Tuple[str, int]:
    value = ""
    length = 0
    for section in textwrap.wrap(bits, 5):
        value += section[1:]
        length += 5
        if section.startswith("0"):
            break
    return bits[length:], int(value, 2)


def parse(bits: str, values: List[int], values_limit: int = 0) -> Tuple[str, List[int]]:
    while bits and int(bits) and not (values_limit and len(values) >= values_limit):
        bits, _ = parse_section(bits, length=3)
        bits, packet_type = parse_section(bits, length=3)
        if packet_type == 4:
            bits, value = parse_literal(bits)
            values.append(value)
        else:
            operation = OPERATIONS[packet_type]
            bits, length_type_id = parse_section(bits, length=1)
            sub_values: List[int] = []
            if length_type_id:
                bits, number_of_subpackages = parse_section(bits, length=11)
                bits, sub_values = parse(
                    bits,
                    sub_values,
                    values_limit=number_of_subpackages,
                )
                values.append(operation(sub_values))
            else:
                bits, length = parse_section(bits, length=15)
                _, sub_values = parse(bits[:length], sub_values)
                bits = bits[length:]
                values.append(operation(sub_values))
    return bits, values


def solve(puzzle_input: Union[str, Path]) -> int:
    _, values = parse(hex_to_bits(read(puzzle_input).strip()), [])
    return values[0]


@pytest.mark.parametrize(
    ("test_input", "expected"),
    TEST_INPUTS,
)
def test(test_input: str, expected: int) -> None:
    assert solve(test_input) == expected


if __name__ == "__main__":
    test_answer = solve(puzzle_input=TEST_INPUTS[-1][0])
    print(test_answer)
    if test_answer == TEST_INPUTS[-1][1]:
        answer = solve(puzzle_input=FILE.parent / "input.txt")
        print(answer)
        submit(answer=answer, file=FILE)
