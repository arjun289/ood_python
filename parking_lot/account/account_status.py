from enum import Enum, auto


class AccountStatus(Enum):
    ACTIVE = auto()
    CLOSED = auto()
    CANCELLED = auto()
    BLACKLISTED = auto()
    NONE = auto()
