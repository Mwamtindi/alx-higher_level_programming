#!/usr/bin/python3
"""
A pytho file containing the class definition of a 'State' and an instance
'Base = declarative_base()'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ :(str) The class-table name
        id :(int) The the class-state id
        name :(str) The class-state name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
