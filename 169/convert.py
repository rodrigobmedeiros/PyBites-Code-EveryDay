
# Same idea of plataform solution
FACTORS = {
    'cm': 2.540,
    'in': 0.3937008 # The problem here is the precision
}

def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()

    # The solution approach was use try/except
    if not (isinstance(value, float) or isinstance(value, int)):
        raise TypeError
    
    # As now, I have keys() I can verify if the fmt is present there.
    if not ('in' in fmt or 'cm' in fmt):
        raise ValueError
    
    factor = FACTORS[fmt]

    return round(value * factor, 4)

