# -*- coding: utf-8 -*-.
from typing import Union

from num_word_converter.errors import (
    ComplexNumberInputError,
    FractionTooLongError,
    NonNumberInputError,
)
from num_word_converter.word2num import WORD_TO_DIGIT

DIGIT_TO_WORD = {scale: word for word, scale in WORD_TO_DIGIT.items()}


def num_to_word(n: Union[float, int]) -> str:
    """
    Recursively convert an integer or decimal number into English words.

    :param n: The number to convert.
    :return: The English words string.
    """
    if not isinstance(n, (int, float)):
        raise NonNumberInputError(
            "`digit_to_word` function takes only integer and float inputs."
        )

    if isinstance(n, complex):
        raise ComplexNumberInputError(
            "`digit_to_word` can't convert complex numbers to words."
        )

    if isinstance(n, float):
        int_part, frac_part = divmod(n, 1)
        frac_part = round(frac_part * 10 ** (len(str(frac_part)) - 2))
        if len(str(frac_part)) > 10:
            raise FractionTooLongError(
                "The fractional part of the input float is too long to convert to words."
            )
        return (
                num_to_word(int_part)
                + " point "
                + " ".join(num_to_word(int(c)) for c in str(frac_part))
        )

    if n < 0:
        return "negative " + num_to_word(abs(n))

    if n < 20:
        return DIGIT_TO_WORD[n]
    elif n < 100:
        if n % 10 == 0:
            return DIGIT_TO_WORD[n]
        else:
            tens = n // 10 * 10
            ones = n % 10
            if ones == 0:
                return DIGIT_TO_WORD[tens]
            else:
                return DIGIT_TO_WORD[tens] + "-" + DIGIT_TO_WORD[ones]
    elif n < 1000:
        if n % 100 == 0:
            return DIGIT_TO_WORD[n // 100] + " hundred"
        elif n % 100 < 10:
            return DIGIT_TO_WORD[n // 100] + " hundred and " + DIGIT_TO_WORD[n % 100]
        else:
            return DIGIT_TO_WORD[n // 100] + " hundred and " + num_to_word(n % 100)
    else:
        num_str = str(int(n))
        groups = (len(num_str) + 2) // 3
        num_str = num_str.zfill(groups * 3)

        word_groups = []
        for i in range(0, len(num_str), 3):
            num_group = int(num_str[i: i + 3])

            if num_group == 0:
                continue

            scale_word = DIGIT_TO_WORD[10 ** (3 * (groups - 1))]
            hundreds_part = num_group // 100 * 100
            ten_and_unit_part = num_group % 100

            if hundreds_part > 0:
                word_groups.append(num_to_word(hundreds_part))
            if ten_and_unit_part != 0:
                if hundreds_part > 0:
                    word_groups.append("and")
                word_groups.append(num_to_word(ten_and_unit_part))

            if scale_word != "one":
                word_groups.append(scale_word)

            groups -= 1

        return " ".join(word_groups).strip()
