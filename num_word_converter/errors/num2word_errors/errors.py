class Error(Exception):
    """Base class for other exceptions"""
    pass


class NonNumberInputError(Error):
    """Raised when the input is not a number (neither int nor float)"""
    pass


class ComplexNumberInputError(Error):
    """Raised when the input is a complex number"""
    pass


class FractionTooLongError(Error):
    """Raised when the fractional part of the input float
    is too long to be converted to words"""
    pass
