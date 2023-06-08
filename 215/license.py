import re


def validate_license(key: str) -> bool:
    """
    Write a regex that matches a PyBites license key (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = '^PB(-[A-Z0-9]{8}){4}$'

    # The point is that I'm validating a complete string end-to-end
    # So I have to put the ^ in the beginning and $ at the end.
    # If not, I can have problems like in the test where the last block has 9 characters.
    return bool(re.match(pattern, key))

