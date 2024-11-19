# -*- coding: utf-8 -*-.
from num_word_converter.consts import UNITS, TENS, SCALES
from num_word_converter.errors import (
    ScaleOutOfOrderError,
    ScaleGapError,
    NoConversionForWordError,
)


WORD_TO_DIGIT = {word: scale for scale, word in enumerate(UNITS)}
WORD_TO_DIGIT.update({word: 10 * scale for scale, word in enumerate(TENS)})
WORD_TO_DIGIT.update(
    {word: 10 ** (scale * 3 or 2) for scale, word in enumerate(SCALES)}
)


def word_to_num(word: str) -> float:
    """
    Convert a string representation of a number into a digit.

    :param word: The word to convert.
    :return: The converted digit.
    """
    word = word.lower()
    if "point" in word:
        whole_part, fractional_part = word.split("point", 1)
        return convert_whole_part_to_digit(
            whole_part.strip()
        ) + convert_fractional_part_to_digit(fractional_part.strip())
    else:
        return convert_whole_part_to_digit(word)


def convert_whole_part_to_digit(word: str) -> int:
    """
    Convert the whole part of a string representation of a number into a digit.

    :param word: The word representing the whole part of the number.
    :return: The converted digit.
    """
    current = result = 0
    previous_scale = None
    for token in word.split():
        if token in WORD_TO_DIGIT:
            scale = WORD_TO_DIGIT[token]
            if token in SCALES:
                if previous_scale and scale <= previous_scale:
                    raise ScaleOutOfOrderError(f"{token} after {previous_scale}")
                current *= scale
                previous_scale = scale
            else:
                if previous_scale and previous_scale >= 1000:
                    raise ScaleGapError(
                        f"Number missing between {previous_scale} and {scale}"
                    )
                current += scale
                previous_scale = None
        else:
            raise NoConversionForWordError("No conversion for " + token)

        if current >= 1000:
            result += current
            current = 0

    return result + current


def convert_fractional_part_to_digit(word: str) -> float:
    """
    Convert the fractional part of a string representation of a number into a digit.

    :param word: The word representing the fractional part of the number.
    :return: The converted digit.
    """
    digits = [convert_whole_part_to_digit(token) for token in word.split()]
    return sum(digit / (10**i) for i, digit in enumerate(digits, start=1))
