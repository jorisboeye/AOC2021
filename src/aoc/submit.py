from pathlib import Path
from typing import Any, Union

from aocd import submit as aocd_submit


def submit(answer: Union[int, str], file: Path, year: int = 2021) -> Any:
    part = "a" if file.stem == "part1" else "b"
    day = int(file.parent.stem[-2:])
    return aocd_submit(answer=answer, part=part, day=day, year=year)
