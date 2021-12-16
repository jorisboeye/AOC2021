import textwrap
from pathlib import Path
from typing import List, Tuple, Union

import pytest

from aoc.parsers import read
from aoc.submit import submit

FILE = Path(__file__)
TEST_RESULT = 16
TEST_INPUTS = (
    ("38006F45291200", 9),
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31),
)


def hex_to_bits(text: str) -> str:
    return "".join((f"{int(h, 16):04b}" for h in text))


def parse_section(bits: str, length: int) -> Tuple[int, str]:
    return int(bits[:length], 2), bits[length:]


def parse_value(bits: str) -> Tuple[int, str]:
    value = ""
    for section in textwrap.wrap(bits, 5):
        value += section
        if section.startswith("0"):
            break
    end_of_value = len(value)
    return int(value, 2), bits[end_of_value:]


def parse(
    bits: str, versions: List[int], values_limit: int = 0
) -> Tuple[str, List[int]]:
    while bits and int(bits) and not (values_limit and len(versions) >= values_limit):
        version, bits = parse_section(bits, length=3)
        versions.append(version)
        packet_type, bits = parse_section(bits, length=3)
        if packet_type == 4:
            _, bits = parse_value(bits)
        else:
            length_type_id, bits = parse_section(bits, length=1)
            if length_type_id:
                number_of_subpackages, bits = parse_section(bits, length=11)
                bits, versions = parse(
                    bits, versions, values_limit=number_of_subpackages
                )
            else:
                length, bits = parse_section(bits, length=15)
                _, versions = parse(bits[:length], versions)
                bits = bits[length:]
    return bits, versions


def solve(puzzle_input: Union[str, Path]) -> int:
    _, versions = parse(hex_to_bits(read(puzzle_input).strip()), [])
    return sum(versions)


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
