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

    clicks = relationship('Clicks', back_populates='link', uselist=False)

    def __init__(self, token: str, long_link: str, activation_date: datetime, deactivation_date: datetime):
        self.token = token
        self.long_link = long_link
        self.activation_date = activation_date
        self.deactivation_date = deactivation_date

    def __repr__(self):
        return f'Link<token={self.token}, long_link={self.long_link}, activation_date={self.activation_date}, deactivation_date={self.deactivation_date}>'


class Clicks(Base):

    clicks_count = Column(Integer)
    link_token = Column(Text, ForeignKey('link.token'), primary_key=True)

    link = relationship("Link", back_populates="clicks")

    def __init__(self, link_token: str, clicks_count: int):
        self.link_token = link_token
        self.clicks_count = clicks_count

    def __repr__(self):
        return f'Clicks<clicks_count={self.clicks_count}>'
