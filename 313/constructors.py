import re

SITE_PROTOCOL = [
    'http://',
    'https://',
    'https:/'
]

class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.pattern = r'.*\.[a-z]{2,3}$'
        self.pattern_matches = re.findall(self.pattern, name)
        
        if not self.pattern_matches:
            raise DomainException
            
        self.name = name
        
    def __str__(self):
        
        return self.pattern_matches[0]
    
    @classmethod
    def parse_url(cls, url):
        
        # identify and replace protocols for empty char
        for protocol in SITE_PROTOCOL:
            
            url = url.replace(protocol, '')
        
        # Ignore if url have additional endpoints information
        url = url.split(r'/')[0]
        
        # Guarantee to get only two terms to define the domain.
        # Example: www.gmail.com will return gmail.com
        domain = '.'.join(url.split('.')[-2:])
        
        return cls(domain)
    
    @classmethod
    def parse_email(cls, email):
        
        domain = email.split('@')[-1]
        
        return cls(domain)