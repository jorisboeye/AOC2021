from functools import singledispatch
from pathlib import Path
from typing import Any, Callable, Iterable, List, Tuple, Union


@singledispatch
def read(arg: Union[Path, str]) -> str:
    raise NotImplementedError(f"Read function not implemented for {type(arg)}")


@read.register  # type: ignore[no-redef]
def _(arg: Path) -> str:
    with open(arg, "r") as file:
        text = file.read()
    return text


@read.register  # type: ignore[no-redef]
def _(arg: str) -> str:
    return arg


def parse_lines(text: str, target: Callable[[str], Any]) -> Iterable[Any]:
    for line in text.strip().split("\n"):
        yield target(line)


def tuple_of_ints(text: str) -> Tuple[int, ...]:
    return tuple(int(number) for number in text.strip().split(","))


def split_mapping(split: str) -> Callable[[str], List[str]]:
    def splitter(text: str) -> List[str]:
        return text.strip().split(split)

    return splitter


def array_generator(
    text: str,
    target: Callable[[str], Any],
    line_splitter: Callable[[str], Iterable[str]],
) -> Iterable[Any]:
    for line in text.strip().splitlines():
        for number in line_splitter(line):
            yield (target(number))


def parse_array(
    text: str,
    target: Callable[[str], Any],
    line_splitter: Callable[[str], Iterable[str]] = lambda x: x,
) -> Tuple[Tuple[int, ...], int]:
    return tuple(
        array_generator(text=text, target=target, line_splitter=line_splitter)
    ), len(text.strip().splitlines()[0])
