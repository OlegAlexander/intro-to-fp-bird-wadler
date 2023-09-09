from typing import NewType
from itertools import chain, islice, pairwise
from more_itertools import split_at, intersperse, flatten
from intro_to_fp_bird_wadler.common import inits

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


if __name__ == "__main__":
    assert normalize("Line   one.\nLine    two.\n\n\nLine   three.") == """Line one.
Line two.

Line three."""

    assert parse("Line one.\nLine two.\n\nLine three.") == [[['Line', 'one.'], ['Line', 'two.']], [['Line', 'three.']]]

    assert countlines("Line one.\nLine two.\n\nLine three.") == 4
    assert countwords("Line one.\nLine two.\n\nLine three.") == 6
    assert countparas("Line one.\nLine two.\n\nLine three.") == 2

    assert paras(lines("Line one.\nLine two.\n\nLine three.")) == [['Line one.', 'Line two.'], ['Line three.']]
    assert unparas(paras(lines("Line one.\nLine two.\n\n\nLine three."))) == ['Line one.', 'Line two.', '', 'Line three.']
    assert unparas(paras(lines("Line one.\nLine one.\n\n\nLine three."))) == ['Line one.', 'Line one.', '', 'Line three.']
    assert deduplicate_empty_strings(list(map(Line, ['Line one.', 'Line two.', '', '', 'Line three.']))) == ['Line one.', 'Line two.', '', 'Line three.']
    assert deduplicate_empty_strings(list(map(Line, ['Line one.', 'Line one.', '', '', 'Line three.']))) == ['Line one.', 'Line one.', '', 'Line three.']

    assert words(Line("This   is a line")) == ['This', 'is', 'a', 'line']
    assert words(Line("line")) == ['line']
    assert unwords(words(Line("This   is a line"))) == "This is a line"

    assert lines("This is a\ntext\n") == ['This is a', 'text', '']
    assert lines("This is a\n\ntext\n") == ['This is a', '', 'text', '']
    assert lines("This is a text") == ['This is a text']
    assert lines("") == ['']
    assert lines("\n") == ['', '']

    assert unlines(lines("This is a\ntext\n")) == "This is a\ntext\n"
    assert unlines(lines("This is a\n\ntext\n")) == "This is a\n\ntext\n"
    assert unlines(lines("This is a text")) == "This is a text"
    assert unlines(lines("")) == ""
    assert unlines(lines("\n")) == "\n"
