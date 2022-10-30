# main.py
# A simple string (time+unit) to seconds converter.
# https://github.com/woidzero/Strime.git


from datetime import datetime
from .exceptions import UnitError
from .converter import converter


class Strime:
    def __init__(self, _prompt: str):
        self._unit = ''.join([i for i in _prompt if not i.isdigit()])
        self._units = [
            "ms",
            "s",
            "m",
            "h",
            "d",
            "w",
            "mn",
            "y",
            "c"
        ]
        
        self._seconds: int = None

        if self._unit not in self._units:
            raise UnitError("'%s' is not correct unit of time." % self._unit)
        else:
            self._value = int(_prompt.replace(self._unit, ''))
            self._seconds = converter(self._value, self._unit)


    @property
    def unit(self):
        return self._unit

    
    @property
    def value(self):
        return self._value


    @property
    def seconds(self):
        return self._seconds