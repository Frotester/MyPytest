from pydantic import BaseModel, validator, field_validator
from src.enums.user_enums import Genders, StatusesLower, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: StatusesLower

    # @field_validator("email")
    # def cheсk_tnat_dog_presented_in_email_address(cls, email):
    #     if "@" in email:
    #         return email
    #     else:
    #         raise ValueError(UserErrors.WRONG_EMAIL.value)



