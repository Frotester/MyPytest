from enum import Enum

from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(PyEnum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MERGED = "MERGED"


class StatusesLower(PyEnum):
    ACTIVE = "ACTIVE".lower()
    BANNED = "BANNED".lower()
    DELETED = "DELETED".lower()
    INACTIVE = "INACTIVE".lower()
    MERGED = "MERGED".lower()

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contail @"


print(Statuses.list())