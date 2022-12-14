from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Link(Base):

    token = Column(Text, primary_key=True, unique=True)
    long_link = Column(Text, unique=True)

    clicks = relationship('Clicks', back_populates='link', uselist=False)

    def __init__(self, token: str, long_link: str):
        self.token = token
        self.long_link = long_link

    def __repr__(self):
        return f'Link<token={self.token}, long_link={self.long_link}>'


class Clicks(Base):

    clicks_count = Column(Integer)
    link_token = Column(Text, ForeignKey('link.token'), primary_key=True)

    link = relationship("Link", back_populates="clicks")

    def __init__(self, link_token: str, clicks_count: int):
        self.link_token = link_token
        self.clicks_count = clicks_count

    def __repr__(self):
        return f'Clicks<clicks_count={self.clicks_count}>'
