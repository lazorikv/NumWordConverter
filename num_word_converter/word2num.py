# -*- coding: utf-8 -*-.
from typing import List, Union, Dict, Final

from num_word_converter.consts import UNITS, TENS, SCALES
from num_word_converter.errors import (
    ScaleOutOfOrderError,
    NoConversionForWordError,
)


WORD_TO_DIGIT: Final[Dict[str, int]] = {word: scale for scale, word in enumerate(UNITS)}
WORD_TO_DIGIT.update({word: 10 * scale for scale, word in enumerate(TENS)})
WORD_TO_DIGIT.update(
    {word: 10 ** (scale * 3 or 2) for scale, word in enumerate(SCALES)}
)


def convert_word_to_digit(word_parts: List[str]) -> int:
    current = result = 0
    previous_token_was_scale = False
    for token in word_parts:
        if token == 'and':
            continue
        if token not in WORD_TO_DIGIT:
            raise NoConversionForWordError(f"No conversion for {token}")
        scale = WORD_TO_DIGIT[token]
        if token in SCALES:
            if previous_token_was_scale:
                raise ScaleOutOfOrderError(f"{token} after scale")
            previous_token_was_scale = True
        else:
            previous_token_was_scale = False
        if current == 0:
            current = scale
        elif scale > current:
            current *= scale
        else:
            current += scale
        if current >= 1000:
            result += current
            current = 0
    return result + current


def word_to_num(word: str) -> Union[int, float]:
    """
    Convert number words into an integer or float
    :param word: str
    :return: Union[int, float]
    """
    if not word or not word.strip():
        raise NoConversionForWordError("Empty string cannot be converted")
        
    word = ' '.join(word.split())
    
    if word.isdigit():
        return int(word)

    # Check if 'point' is in the word. If so, we have a decimal number
    if "point" in word:
        whole, frac = word.split("point")
        whole = whole.strip()
        frac = frac.strip()

        whole_parts = whole.replace("-", " ").lower().split()
        frac_parts = frac.replace("-", " ").lower().split()

        return convert_word_to_digit(whole_parts) + convert_word_to_digit(frac_parts) * 10 ** (-len(frac_parts))

    # Handle compound numbers (numbers that are hyphenated)
    word = word.replace("-", " ")

    word_parts = word.lower().split()
    return convert_word_to_digit(word_parts)


def convert_fractional_part_to_digit(word_parts: List[str]) -> float:
    """
    Convert the fractional part of a string representation of a number into a digit.

    :param word_parts: The words representing the fractional part of the number.
    :return: The converted digit.
    """
    digits = [convert_word_to_digit([token]) for token in word_parts]
    return sum(digit / (10 ** i) for i, digit in enumerate(digits, start=1))

