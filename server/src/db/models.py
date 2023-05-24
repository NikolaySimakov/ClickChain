from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base
from resources.constants import LINK_TOKEN_MAX_LENGTH


class Link(Base):

    token = Column(String(LINK_TOKEN_MAX_LENGTH),
                   primary_key=True, unique=True)
    long_link = Column(Text, unique=True)
    activation_date = Column(DateTime)
    deactivation_date = Column(DateTime)

    clicks = relationship("Click", back_populates="link")

    def __init__(self, token: str, long_link: str, activation_date: datetime, deactivation_date: datetime):
        self.token = token
        self.long_link = long_link
        self.activation_date = activation_date
        self.deactivation_date = deactivation_date

    def __repr__(self):
        return f'Link<token={self.token}, long_link={self.long_link}, activation_date={self.activation_date}, deactivation_date={self.deactivation_date}>'


class Click(Base):

    id = Column(Integer, index=True, primary_key=True, unique=True)
    link_token = Column(String(LINK_TOKEN_MAX_LENGTH),
                        ForeignKey('link.token'))
    user_ip = Column(String(15))
    date = Column(DateTime)

    link = relationship("Link", back_populates="clicks")

    def __init__(self, link_token: str, user_ip: str, date: datetime):
        self.link_token = link_token
        self.user_ip = user_ip
        self.date = date

    def __repr__(self):
        return f'Clicks<user_ip={self.user_ip}, date={self.date}>'
