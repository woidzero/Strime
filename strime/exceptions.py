# converter.py
# A simple string (time+unit) to seconds converter.
# https://github.com/woidzero/Strime.git


class UnitError(BaseException):
    def __init__(self, *args: object):
        self.args = args
    
    def __str__(self):
        return "UnitError: ".join([*self.args])