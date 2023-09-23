from intro_to_fp_bird_wadler.ch4.text_processing import (
    normalize, parse, filltext, lines, unlines, words, unwords, paras,
    unparas, countlines, countwords, countparas, deduplicate_empty_strings, Line
)


def test_all() -> None:

    assert filltext(72, """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac facilisis lorem. Pellentesque ullamcorper posuere nulla, quis rutrum mi. Mauris nec massa imperdiet, porttitor leo ut, venenatis enim. Aliquam ullamcorper, enim et imperdiet pharetra, purus mauris semper lacus, vitae condimentum orci nisl bibendum mauris. Pellentesque eleifend tellus sit amet dui mollis, a dignissim lacus ultrices.\n\nSuspendisse in massa nec nisi cursus egestas. Nam justo arcu, imperdiet ac lorem a, lobortis aliquam purus. Duis eu erat at lacus consequat posuere eu at elit. Ut eget urna eu lacus fermentum rhoncus. Donec ultrices erat id eros convallis consequat. Vivamus ut maximus eros. Etiam quis sapien aliquam, molestie dolor tincidunt, lacinia ipsum. Suspendisse at aliquam purus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer aliquet lacus purus, quis dapibus lorem elementum id. Nunc ut lacus nec nisi fermentum posuere vel sit amet nunc.""") == """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac
facilisis lorem. Pellentesque ullamcorper posuere nulla, quis rutrum mi.
Mauris nec massa imperdiet, porttitor leo ut, venenatis enim. Aliquam
ullamcorper, enim et imperdiet pharetra, purus mauris semper lacus,
vitae condimentum orci nisl bibendum mauris. Pellentesque eleifend
tellus sit amet dui mollis, a dignissim lacus ultrices.

Suspendisse in massa nec nisi cursus egestas. Nam justo arcu, imperdiet
ac lorem a, lobortis aliquam purus. Duis eu erat at lacus consequat
posuere eu at elit. Ut eget urna eu lacus fermentum rhoncus. Donec
ultrices erat id eros convallis consequat. Vivamus ut maximus eros.
Etiam quis sapien aliquam, molestie dolor tincidunt, lacinia ipsum.
Suspendisse at aliquam purus. Interdum et malesuada fames ac ante ipsum
primis in faucibus. Integer aliquet lacus purus, quis dapibus lorem
elementum id. Nunc ut lacus nec nisi fermentum posuere vel sit amet
nunc."""

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
