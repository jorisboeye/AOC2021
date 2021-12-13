from functools import singledispatch
from pathlib import Path


@singledispatch
def read(arg):
    raise NotImplementedError(f"Read function not implemented for {type(arg)}")


@read.register
def _(arg: Path):
    with open(arg, "r") as file:
        text = file.read()
    return text


@read.register
def _(arg: str):
    return arg
