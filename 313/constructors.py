import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        
    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively