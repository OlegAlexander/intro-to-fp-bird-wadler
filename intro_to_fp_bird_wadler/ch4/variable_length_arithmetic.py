from itertools import dropwhile, repeat
from more_itertools import take, last
from operator import eq, gt, lt, ne, ge, le, add, sub, neg
from typing import Callable, cast
from functools import partial, reduce
from intro_to_fp_bird_wadler.common import drop, foldr, zip_with, fst, snd, scan

BASE = 10


def strep(xs: list[int]) -> list[int]:
    '''Drop leading zeros'''
    ys = list(dropwhile(lambda x: x == 0, xs))
    return [0] if ys == [] else ys


def align(xs: list[int], ys: list[int]) -> tuple[list[int], list[int]]:
    '''Align lists by adding leading zeros'''
    n = len(ys) - len(xs)
    if n > 0:
        return (list(repeat(0, n)) + xs, ys)
    else:
        return (xs, list(repeat(0, -n)) + ys)


CompareOp = Callable[[list[int], list[int]], bool]


def vcompare(op: CompareOp, xs: list[int], ys: list[int]) -> bool:
    '''Compare variable length numbers'''
    us, vs = align(xs, ys)
    return op(us, vs)


veq = cast(CompareOp, partial(vcompare, eq))
vgt = cast(CompareOp, partial(vcompare, gt))
vlt = cast(CompareOp, partial(vcompare, lt))  # vless
vne = cast(CompareOp, partial(vcompare, ne))
vge = cast(CompareOp, partial(vcompare, ge))
vle = cast(CompareOp, partial(vcompare, le))


def carry(x: int, xs_: list[int]) -> list[int]:
    '''Add carry to list of digits'''
    c, *xs = xs_
    return [(x + c) // BASE] + [(x + c) % BASE] + xs


def norm(xs: list[int]) -> list[int]:
    '''Normalize list of digits'''
    return strep(foldr(carry, [0], xs))


def vadd(xs: list[int], ys: list[int]) -> list[int]:
    '''Add variable length numbers'''
    return norm(zip_with(add, align(xs, ys)))


def vsub(xs: list[int], ys: list[int]) -> list[int]:
    '''Subtract variable length numbers'''
    return norm(zip_with(sub, align(xs, ys)))


def negative(xs: list[int]) -> bool:
    return xs[0] < 0


def negate(xs: list[int]) -> list[int]:
    # neg needs a type: ignore, so I used a lambda
    return norm(list(map(lambda x: -x, xs)))


def bmul(xs: list[int], y: int) -> list[int]:
    return norm(list(map(lambda x: x * y, xs)))


def psums(xs: list[int], ys: list[int]) -> list[int]:
    '''Partial sums of two lists'''
    return list(map(lambda y: bmul(xs, y), ys))  # type: ignore


def shift_add(xs: list[int], ys: list[int]) -> list[int]:
    '''Add two lists by shifting and adding'''
    return vadd(xs + [0], ys)


def vmul(xs: list[int], ys: list[int]) -> list[int]:
    '''Multiply variable length numbers'''
    return reduce(shift_add, psums(xs, ys))  # type: ignore


def astep(xs: list[int], ys: list[int]) -> tuple[int, list[int]]:
    return (0, xs)


def bstep(xs: list[int], ys: list[int]) -> tuple[int, list[int]]:
    zs = vsub(xs, ys)
    return (0, xs) if negative(zs) else (1, zs)


def cstep(xs: list[int], ys: list[int]) -> tuple[int, list[int]]:
    q = guess(xs, ys) - 2
    rs0 = vsub(xs, bmul(ys, q))
    rs1 = vsub(rs0, ys)
    rs2 = vsub(rs1, ys)
    if vlt(rs0, ys):
        return (q, rs0)
    elif vlt(rs1, ys):
        return (q + 1, rs1)
    else:
        return (q + 2, rs2)


def dstep(ys: list[int], q_rs: tuple[int, list[int]], x: int) -> tuple[int, list[int]]:
    q, rs = q_rs
    xs = rs + [x]
    if len(xs) < len(ys):
        return astep(xs, ys)
    if len(xs) == len(ys):
        return bstep(xs, ys)
    if len(xs) == len(ys) + 1:
        return cstep(xs, ys)
    assert False  # unreachable


def guess(xs_: list[int], ys_: list[int]) -> int:
    x0, x1, *xs = xs_
    y1, *ys = ys_
    return BASE - 1 if x0 >= y1 else (x0 * BASE + x1) // y1


def divalg(xs: list[int], ys: list[int]) -> list[tuple[int, list[int]]]:
    m = len(ys) - 1
    return list(scan(partial(dstep, ys), (0, take(m, xs)), drop(m, xs)))


def bqrm(x_xs: list[int], d: int) -> tuple[list[int], int]:
    x, *xs = x_xs
    f = lambda r, x: BASE * (r % d) + x
    rs = list(scan(f, x, xs))
    qs = list(map(lambda r: r // d, rs))
    if len(xs) > 0:
        return (strep(qs), last(rs) % d)
    else:
        return ([x // d], x % d)


def bdiv(xs: list[int], d: int) -> list[int]:
    return fst(bqrm(xs, d))


def bmod(xs: list[int], d: int) -> int:
    return snd(bqrm(xs, d))


def vqrm(xs: list[int], ys: list[int]) -> tuple[list[int], list[int]]:
    d = BASE // (ys[0] + 1)
    ds = divalg(bmul(xs, d), bmul(ys, d))
    rs = bdiv(snd(last(ds)), d)
    qs = list(map(fst, ds))  # type: ignore
    return (strep(qs), strep(rs))  # type: ignore
