from functools import singledispatch
from pathlib import Path
from typing import Any, Callable, Iterable, Tuple, Union


@singledispatch
def read(arg: Union[Path, str]) -> str:
    raise NotImplementedError(f"Read function not implemented for {type(arg)}")


@read.register
def _(arg: Path) -> str:
    with open(arg, "r") as file:
        text = file.read()
    return text


@read.register
def _(arg: str) -> str:
    return arg


def parse_lines(text: str, function: Callable[[str], Any]) -> Iterable[Any]:
    for line in text.strip().split("\n"):
        yield function(line)


def tuple_of_ints(text: str) -> Tuple[int, ...]:
    return tuple(int(number) for number in text.strip().split(","))
