from typing import Callable, TypeVar
from functools import reduce
from itertools import accumulate, islice

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


def drop(n: int, xs: list[T]) -> list[T]:
    return list(islice(xs, n, None))


def foldr(f: Callable[[T, U], U], acc: U, xs: list[T]) -> U:
    return reduce(lambda x, y: f(y, x), reversed(xs), acc)


def zip_with(f: Callable[[T, U], V], xs_ys: tuple[list[T], list[U]]) -> list[V]:
    xs, ys = xs_ys
    return list(map(f, xs, ys))


def fst(pair: tuple[T, U]) -> T:
    return pair[0]


def snd(pair: tuple[T, U]) -> U:
    return pair[1]


def scan(f: Callable[[T, U], T], acc: T, xs: list[U]) -> list[T]:
    return list(accumulate(xs, lambda x, y: f(x, y), initial=acc))


def inits(it: list[T]) -> list[list[T]]:
    """Source: https://stackoverflow.com/a/33332733"""
    return [list(it[:i]) for i in range(len(it) + 1)]
