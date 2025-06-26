from pydantic import BaseModel, validator, field_validator
from src.enums.user_enams import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator("email")
    def chek_tnat_dog_presented_in_email_address(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

