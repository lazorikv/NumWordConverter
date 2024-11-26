# -*- coding: utf-8 -*-.
import math
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
    Convert a number to its word representation in English.
    
    Args:
        n: Number to convert (integer or float)
        
    Returns:
        str: Word representation of the number
        
    Raises:
        NonNumberInputError: If input is not a number
        ComplexNumberInputError: If input is a complex number
        FractionTooLongError: If fractional part is too long
    
    Examples:
        >>> num_to_word(42)
        'forty-two'
        >>> num_to_word(3.14)
        'three point one four'
    """
    if not isinstance(n, (int, float)):
        raise NonNumberInputError(
            "`digit_to_word` function takes only integer and float inputs."
        )

    if isinstance(n, complex):
        raise ComplexNumberInputError(
            "`digit_to_word` can't convert complex numbers to words."
        )

    if isinstance(n, float) and (n.is_integer() or math.isinf(n) or math.isnan(n)):
        raise NonNumberInputError("NaN and Infinity are not supported")

    if isinstance(n, float):
        n = round(n, 10)
        int_part = int(n)
        frac_part = abs(n - int_part)
        
        frac_str = f'{frac_part:.10f}'.rstrip('0').split('.')[1]
        
        if len(frac_str) > 10:
            raise FractionTooLongError(
                "The fractional part of the input float is too long to convert to words."
            )
            
        return (
            num_to_word(int_part)
            + " point "
            + " ".join(num_to_word(int(d)) for d in frac_str)
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
