class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoConversionForWordError(Error):
    """Raised when a word cannot be converted to a number"""
    pass


class ScaleOutOfOrderError(Error):
    """Raised when the scale words are given in wrong order, like "thousand hundred" instead of "hundred thousand" """
    pass


class ScaleGapError(Error):
    """Raised when there is a gap between scale words, like "hundred thousand" with missing tens"""
    pass
