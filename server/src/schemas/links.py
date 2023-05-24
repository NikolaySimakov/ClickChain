from pydantic import BaseModel, validator, constr, HttpUrl
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

    @validator('deactivation_date')
    def deactivation_date_must_be_later(cls, v, values):
        if 'activation_date' in values and v <= values['activation_date']:
            raise ValueError(strings.WRONG_DEACTIVATION_DATE)
        return v

    class Config:
        orm_mode = True


class Click(BaseModel):

    link_token: str
    user_ip: str
    date: datetime

    @validator('user_ip')
    def validate_user_ip(cls, v):
        return constr(regex=r'^(\d{1,3}\.){3}\d{1,3}$|^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')(v)

    class Config:
        orm_mode = True
