from intro_to_fp_bird_wadler.ch4.numbers_to_words import convert


def test_convert() -> None:
    actual = [convert(i) for i in range(1, 1_000_000, 9999)]
    expected = ['one',
                'ten thousand',
                'nineteen thousand nine hundred and ninety-nine',
                'twenty-nine thousand nine hundred and ninety-eight',
                'thirty-nine thousand nine hundred and ninety-seven',
                'forty-nine thousand nine hundred and ninety-six',
                'fifty-nine thousand nine hundred and ninety-five',
                'sixty-nine thousand nine hundred and ninety-four',
                'seventy-nine thousand nine hundred and ninety-three',
                'eighty-nine thousand nine hundred and ninety-two',
                'ninety-nine thousand nine hundred and ninety-one',
                'one hundred and nine thousand nine hundred and ninety',
                'one hundred and nineteen thousand nine hundred and eighty-nine',
                'one hundred and twenty-nine thousand nine hundred and eighty-eight',
                'one hundred and thirty-nine thousand nine hundred and eighty-seven',
                'one hundred and forty-nine thousand nine hundred and eighty-six',
                'one hundred and fifty-nine thousand nine hundred and eighty-five',
                'one hundred and sixty-nine thousand nine hundred and eighty-four',
                'one hundred and seventy-nine thousand nine hundred and eighty-three',
                'one hundred and eighty-nine thousand nine hundred and eighty-two',
                'one hundred and ninety-nine thousand nine hundred and eighty-one',
                'two hundred and nine thousand nine hundred and eighty',
                'two hundred and nineteen thousand nine hundred and seventy-nine',
                'two hundred and twenty-nine thousand nine hundred and seventy-eight',
                'two hundred and thirty-nine thousand nine hundred and seventy-seven',
                'two hundred and forty-nine thousand nine hundred and seventy-six',
                'two hundred and fifty-nine thousand nine hundred and seventy-five',
                'two hundred and sixty-nine thousand nine hundred and seventy-four',
                'two hundred and seventy-nine thousand nine hundred and seventy-three',
                'two hundred and eighty-nine thousand nine hundred and seventy-two',
                'two hundred and ninety-nine thousand nine hundred and seventy-one',
                'three hundred and nine thousand nine hundred and seventy',
                'three hundred and nineteen thousand nine hundred and sixty-nine',
                'three hundred and twenty-nine thousand nine hundred and sixty-eight',
                'three hundred and thirty-nine thousand nine hundred and sixty-seven',
                'three hundred and forty-nine thousand nine hundred and sixty-six',
                'three hundred and fifty-nine thousand nine hundred and sixty-five',
                'three hundred and sixty-nine thousand nine hundred and sixty-four',
                'three hundred and seventy-nine thousand nine hundred and sixty-three',
                'three hundred and eighty-nine thousand nine hundred and sixty-two',
                'three hundred and ninety-nine thousand nine hundred and sixty-one',
                'four hundred and nine thousand nine hundred and sixty',
                'four hundred and nineteen thousand nine hundred and fifty-nine',
                'four hundred and twenty-nine thousand nine hundred and fifty-eight',
                'four hundred and thirty-nine thousand nine hundred and fifty-seven',
                'four hundred and forty-nine thousand nine hundred and fifty-six',
                'four hundred and fifty-nine thousand nine hundred and fifty-five',
                'four hundred and sixty-nine thousand nine hundred and fifty-four',
                'four hundred and seventy-nine thousand nine hundred and fifty-three',
                'four hundred and eighty-nine thousand nine hundred and fifty-two',
                'four hundred and ninety-nine thousand nine hundred and fifty-one',
                'five hundred and nine thousand nine hundred and fifty',
                'five hundred and nineteen thousand nine hundred and forty-nine',
                'five hundred and twenty-nine thousand nine hundred and forty-eight',
                'five hundred and thirty-nine thousand nine hundred and forty-seven',
                'five hundred and forty-nine thousand nine hundred and forty-six',
                'five hundred and fifty-nine thousand nine hundred and forty-five',
                'five hundred and sixty-nine thousand nine hundred and forty-four',
                'five hundred and seventy-nine thousand nine hundred and forty-three',
                'five hundred and eighty-nine thousand nine hundred and forty-two',
                'five hundred and ninety-nine thousand nine hundred and forty-one',
                'six hundred and nine thousand nine hundred and forty',
                'six hundred and nineteen thousand nine hundred and thirty-nine',
                'six hundred and twenty-nine thousand nine hundred and thirty-eight',
                'six hundred and thirty-nine thousand nine hundred and thirty-seven',
                'six hundred and forty-nine thousand nine hundred and thirty-six',
                'six hundred and fifty-nine thousand nine hundred and thirty-five',
                'six hundred and sixty-nine thousand nine hundred and thirty-four',
                'six hundred and seventy-nine thousand nine hundred and thirty-three',
                'six hundred and eighty-nine thousand nine hundred and thirty-two',
                'six hundred and ninety-nine thousand nine hundred and thirty-one',
                'seven hundred and nine thousand nine hundred and thirty',
                'seven hundred and nineteen thousand nine hundred and twenty-nine',
                'seven hundred and twenty-nine thousand nine hundred and twenty-eight',
                'seven hundred and thirty-nine thousand nine hundred and twenty-seven',
                'seven hundred and forty-nine thousand nine hundred and twenty-six',
                'seven hundred and fifty-nine thousand nine hundred and twenty-five',
                'seven hundred and sixty-nine thousand nine hundred and twenty-four',
                'seven hundred and seventy-nine thousand nine hundred and twenty-three',
                'seven hundred and eighty-nine thousand nine hundred and twenty-two',
                'seven hundred and ninety-nine thousand nine hundred and twenty-one',
                'eight hundred and nine thousand nine hundred and twenty',
                'eight hundred and nineteen thousand nine hundred and nineteen',
                'eight hundred and twenty-nine thousand nine hundred and eighteen',
                'eight hundred and thirty-nine thousand nine hundred and seventeen',
                'eight hundred and forty-nine thousand nine hundred and sixteen',
                'eight hundred and fifty-nine thousand nine hundred and fifteen',
                'eight hundred and sixty-nine thousand nine hundred and fourteen',
                'eight hundred and seventy-nine thousand nine hundred and thirteen',
                'eight hundred and eighty-nine thousand nine hundred and twelve',
                'eight hundred and ninety-nine thousand nine hundred and eleven',
                'nine hundred and nine thousand nine hundred and ten',
                'nine hundred and nineteen thousand nine hundred and nine',
                'nine hundred and twenty-nine thousand nine hundred and eight',
                'nine hundred and thirty-nine thousand nine hundred and seven',
                'nine hundred and forty-nine thousand nine hundred and six',
                'nine hundred and fifty-nine thousand nine hundred and five',
                'nine hundred and sixty-nine thousand nine hundred and four',
                'nine hundred and seventy-nine thousand nine hundred and three',
                'nine hundred and eighty-nine thousand nine hundred and two',
                'nine hundred and ninety-nine thousand nine hundred and one']
    assert actual == expected