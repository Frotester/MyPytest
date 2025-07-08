from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(Enum):
    inactive = "inactive"
    ACTIVE = "active"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contail @"
