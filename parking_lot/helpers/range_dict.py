class RangeDict(dict):
    """
    A collection which contains range as keys and corresponding values of 
    any type.

    It returns a value from the dict for an item which falls into one of
    the ranges.
    """

    def __getitem__(self, item):
        if not isinstance(item, range):  # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
