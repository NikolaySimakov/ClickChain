from pydantic import BaseModel, validator, HttpUrl
from datetime import datetime

from resources import strings, constants


class LongLink(BaseModel):

    link: HttpUrl

    class Config:
        schema_extra = {
            "link": "https://your.very/long?q=link/jnknK%WBKbWK#Fwjbkf%kjf#bkjwekjDBWE#KBJw#kd%wjb"
        }


class LinkBase(BaseModel):

    token: str
    long_link: HttpUrl

    @validator('token')
    def validate_token_lenth(cls, v):

        if len(v) < constants.LINK_TOKEN_MIN_LENGTH:
            raise ValueError(strings.SHORT_TOKEN)

        elif len(v) > constants.LINK_TOKEN_MAX_LENGTH:
            raise ValueError(strings.LONG_TOKEN)

        return v


class Link(LinkBase):

    activation_date: datetime
    deactivation_date: datetime

    class Config:
        orm_mode = True


# TODO: - Add to clicks schema user ip and datetime of click

class ClicksBase(BaseModel):

    link_token: str
    clicks_count: int

    class Config:
        orm_mode = True
