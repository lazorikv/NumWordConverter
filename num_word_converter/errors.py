class BaseError(Exception):
    """Base class for all converter errors"""
    pass


# num2word errors
class NonNumberInputError(BaseError):
    """Raised when input is not a number"""
    pass


class ComplexNumberInputError(BaseError):
    """Raised when trying to convert a complex number"""
    pass


class FractionTooLongError(BaseError):
    """Raised when the fractional part is too long"""
    pass


# word2num errors
class ScaleOutOfOrderError(BaseError):
    """Raised when scale words are in wrong order"""
    pass


class NoConversionForWordError(BaseError):
    """Raised when a word cannot be converted"""
    pass
