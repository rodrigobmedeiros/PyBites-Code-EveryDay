from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name: str, expires: datetime):

        self.name = name
        self._expired = expires < NOW

    @property
    def expired(self):

        return self._expired

