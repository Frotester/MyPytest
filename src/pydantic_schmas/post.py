from pydantic import BaseModel, validator, field_validator, Field


class Post(BaseModel):
    id: int = Field(le=4)
    title: str

    # @field_validator("id")
    # def check_that_id_is_less_two(cls, v):
    #     if v > 2:
    #         raise ValueError("Id is not less tnab two")
    #     else:
    #         return v