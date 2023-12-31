from typing import NewType
from itertools import chain, islice, pairwise
from more_itertools import split_at, intersperse, flatten, take
from intro_to_fp_bird_wadler.common import inits, drop

Line = NewType('Line', str)
Word = NewType('Word', str)
Para = NewType('Para', list[Line])


def lines(text: str) -> list[Line]:
    return [Line(s) for s in text.split('\n')]


def unlines(lines: list[Line]) -> str:
    return '\n'.join(lines)


def words(line: Line) -> list[Word]:
    return [Word(s) for s in line.split()]


def unwords(ws: list[Word]) -> Line:
    return Line(' '.join(ws))


def paras(lines: list[Line]) -> list[Para]:
    return [Para(p)
            for p
            in split_at(lines, lambda line: line == '')]


def deduplicate_empty_strings(lines: list[Line]) -> list[Line]:
    """I added this because this is probably what the authors meant to do?
    Runs of spaces are collapsed into a single space, so why not runs of empty lines?"""
    paired = pairwise(lines + [""])
    return [Line(s) for s, next_s in paired if s != "" or next_s != ""]


def unparas(paras: list[Para]) -> list[Line]:
    return deduplicate_empty_strings(list(flatten(intersperse([Line('')], paras))))


def countlines(text: str) -> int:
    return len(lines(text))


def countwords(text: str) -> int:
    return len(list(flatten(map(words, lines(text)))))


def countparas(text: str) -> int:
    return len(paras(lines(text)))


def parse(text: str) -> list[list[list[Word]]]:
    return list(map(lambda para: list(map(words, para)), paras(lines(text))))


def unparse(paras: list[list[list[Word]]]) -> str:
    return unlines(unparas(
        list(map(lambda para: Para(list(map(unwords, para))), paras))))


def normalize(text: str) -> str:
    return unparse(parse(text))


def greedy(line_length: int, words: list[Word]) -> int:
    """Greedy algorithm for line breaking."""
    return max([len(us) for us in inits(words) if len(unwords(us)) <= line_length])


def fill(line_length: int, words: list[Word]) -> list[list[Word]]:
    if len(words) == 0:
        return []
    else:
        n = greedy(line_length, words)
        first_line = take(n, words)
        rest_words = drop(n, words)
        return [first_line] + fill(line_length, rest_words)


def linewords(lines: list[Line]) -> list[Word]:
    return list(flatten(map(words, lines)))


def textparas(text: str) -> list[list[Word]]:
    return list(map(linewords, paras(lines(text))))


def filltext(line_length: int, text: str) -> str:
    return unparse(list(map(lambda words: fill(line_length, words), textparas(text))))
