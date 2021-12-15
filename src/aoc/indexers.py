from functools import lru_cache
from typing import Callable, Set, Tuple


def get_relative_positions(line_length: int, shape: str) -> Tuple[int, ...]:
    if shape == "diamond":
        return (-line_length, -1, +1, line_length)
    elif shape == "square":
        return (
            -line_length - 1,
            -line_length,
            -line_length + 1,
            -1,
            +1,
            line_length - 1,
            line_length,
            line_length + 1,
        )
    else:
        raise ValueError(f"Shape <{shape}> doesn't esxist")


def neighbors(
    numbers: Tuple[int, ...], line_length: int, shape: str
) -> Callable[[int], Set[int]]:
    relative_positions = get_relative_positions(line_length=line_length, shape=shape)
    max_length = len(numbers)

    @lru_cache(maxsize=None)
    def indexer(idx: int) -> Set[int]:
        results = set()
        col = idx % line_length
        positions = [idx + x for x in relative_positions]
        for pos in positions:
            poscol = pos % line_length
            if pos >= 0 and pos < max_length and abs(poscol - col) < 2:
                results.add(pos)
        return results

    return indexer
